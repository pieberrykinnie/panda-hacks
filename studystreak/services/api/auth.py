"""
JWT Authentication middleware for StudyStreak API.

This module provides JWT validation for Supabase authentication tokens,
including middleware to protect API routes and extract user information.
"""

import os
import json
from typing import Optional, Dict, Any
from urllib.parse import urljoin

import httpx
from fastapi import HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import BaseModel

# Security scheme for JWT tokens
security = HTTPBearer()

class UserInfo(BaseModel):
    """User information extracted from JWT token."""
    id: str
    email: str
    aud: str
    exp: int
    sub: str
    user_metadata: Optional[Dict[str, Any]] = None
    app_metadata: Optional[Dict[str, Any]] = None

class AuthError(BaseModel):
    """Authentication error response."""
    error: str
    message: str

def get_supabase_jwks_url() -> str:
    """Get Supabase JWKS URL from environment variables."""
    supabase_url = os.getenv("SUPABASE_URL")
    if not supabase_url:
        raise ValueError("SUPABASE_URL environment variable is required")
    return urljoin(supabase_url, "/rest/v1/auth/jwks")

def get_supabase_anon_key() -> str:
    """Get Supabase anonymous key from environment variables."""
    anon_key = os.getenv("SUPABASE_ANON_KEY")
    if not anon_key:
        raise ValueError("SUPABASE_ANON_KEY environment variable is required")
    return anon_key

async def fetch_jwks() -> Dict[str, Any]:
    """Fetch JSON Web Key Set from Supabase."""
    jwks_url = get_supabase_jwks_url()
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(jwks_url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch JWKS from Supabase: {str(e)}"
            )

def get_key_from_jwks(jwks: Dict[str, Any], kid: str) -> Optional[str]:
    """Extract the public key from JWKS using the key ID."""
    for key in jwks.get("keys", []):
        if key.get("kid") == kid:
            return key
    return None

async def verify_jwt_token(token: str) -> UserInfo:
    """
    Verify and decode a Supabase JWT token.
    
    Args:
        token: The JWT token to verify
        
    Returns:
        UserInfo: Decoded user information
        
    Raises:
        HTTPException: If token is invalid or verification fails
    """
    try:
        # Decode the token header to get the key ID
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        
        if not kid:
            raise HTTPException(
                status_code=401,
                detail="Invalid token: missing key ID"
            )
        
        # Fetch JWKS from Supabase
        jwks = await fetch_jwks()
        key_data = get_key_from_jwks(jwks, kid)
        
        if not key_data:
            raise HTTPException(
                status_code=401,
                detail="Invalid token: key not found in JWKS"
            )
        
        # Verify and decode the token
        payload = jwt.decode(
            token,
            key_data,
            algorithms=["RS256"],
            audience="authenticated",
            issuer="https://supabase.co"
        )
        
        # Extract user information
        user_info = UserInfo(
            id=payload.get("sub", ""),
            email=payload.get("email", ""),
            aud=payload.get("aud", ""),
            exp=payload.get("exp", 0),
            sub=payload.get("sub", ""),
            user_metadata=payload.get("user_metadata"),
            app_metadata=payload.get("app_metadata")
        )
        
        return user_info
        
    except HTTPException:
        raise
    except JWTError as e:
        raise HTTPException(
            status_code=401,
            detail=f"Invalid token: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Token verification failed: {str(e)}"
        )

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UserInfo:
    """
    Dependency to get the current authenticated user.
    
    Args:
        credentials: HTTP Bearer token credentials
        
    Returns:
        UserInfo: Current user information
        
    Raises:
        HTTPException: If authentication fails
    """
    token = credentials.credentials
    return await verify_jwt_token(token)

def require_auth(func):
    """
    Decorator to require authentication for API endpoints.
    
    Usage:
        @app.get("/protected")
        @require_auth
        async def protected_endpoint(user: UserInfo = Depends(get_current_user)):
            return {"message": f"Hello {user.email}"}
    """
    return func