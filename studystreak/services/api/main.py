"""
StudyStreak API Service

FastAPI service with JWT authentication middleware for Supabase integration.
Provides protected endpoints for study plans and user management.
"""

import os
from typing import Dict, Any

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from auth import get_current_user, UserInfo, AuthError

# Load environment variables
load_dotenv()

app = FastAPI(
    title="StudyStreak API",
    description="API service for StudyStreak - gamified study planning platform",
    version="1.0.0"
)

# Configure CORS for web app integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative dev port
        os.getenv("WEB_APP_URL", "https://studystreak.fly.dev")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_class=JSONResponse)
def health() -> Dict[str, Any]:
    """Health check endpoint for API service."""
    return {
        "status": "ok",
        "service": "studystreak-api",
        "version": "1.0.0"
    }

@app.get("/auth/me", response_class=JSONResponse)
async def get_current_user_info(user: UserInfo = Depends(get_current_user)) -> Dict[str, Any]:
    """
    Get current user information from JWT token.
    
    This endpoint demonstrates JWT validation and returns user data
    extracted from the authenticated token.
    """
    return {
        "user": {
            "id": user.id,
            "email": user.email,
            "metadata": user.user_metadata
        },
        "authenticated": True
    }

@app.get("/api/plans", response_class=JSONResponse)
async def list_user_plans(user: UserInfo = Depends(get_current_user)) -> Dict[str, Any]:
    """
    List study plans for the authenticated user.
    
    This is a protected endpoint that requires valid JWT authentication.
    In the full implementation, this would query the database for user plans.
    """
    # TODO: Implement database query for user plans
    return {
        "plans": [],
        "user_id": user.id,
        "message": "Plans endpoint - database integration pending"
    }

@app.post("/api/plans", response_class=JSONResponse)
async def create_plan(
    plan_data: Dict[str, Any],
    user: UserInfo = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Create a new study plan for the authenticated user.
    
    This is a protected endpoint that requires valid JWT authentication.
    In the full implementation, this would save the plan to the database.
    """
    # TODO: Implement database save for new plan
    return {
        "plan_id": "temp-id",
        "user_id": user.id,
        "title": plan_data.get("title", "Untitled Plan"),
        "message": "Plan creation - database integration pending"
    }

@app.get("/api/streaks", response_class=JSONResponse)
async def get_user_streaks(user: UserInfo = Depends(get_current_user)) -> Dict[str, Any]:
    """
    Get streak information for the authenticated user.
    
    This is a protected endpoint that requires valid JWT authentication.
    In the full implementation, this would query the database for user streaks.
    """
    # TODO: Implement database query for user streaks
    return {
        "streaks": [],
        "user_id": user.id,
        "message": "Streaks endpoint - database integration pending"
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom exception handler for authentication errors."""
    if exc.status_code == 401:
        return JSONResponse(
            status_code=401,
            content=AuthError(
                error="unauthorized",
                message="Invalid or missing authentication token"
            ).dict()
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

if __name__ == "__main__":
    import uvicorn
    
    # Validate required environment variables
    required_env_vars = ["SUPABASE_URL", "SUPABASE_ANON_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {missing_vars}")
        print("Please set SUPABASE_URL and SUPABASE_ANON_KEY environment variables")
        exit(1)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )