"""
Tests for StudyStreak API main endpoints.

Tests cover health checks, authentication endpoints, and protected routes.
"""

from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from fastapi import Depends

from main import app
from auth import UserInfo, get_current_user

client = TestClient(app)

def test_health() -> None:
    """Test the /health endpoint returns status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "studystreak-api"
    assert data["version"] == "1.0.0"

def test_protected_endpoints_require_auth() -> None:
    """Test that protected endpoints return 403 without authentication."""
    protected_endpoints = [
        "/auth/me",
        "/api/plans",
        "/api/streaks"
    ]
    
    for endpoint in protected_endpoints:
        response = client.get(endpoint)
        assert response.status_code == 403
        assert "Not authenticated" in response.json()["error"]

def test_auth_me_endpoint_with_mock_user() -> None:
    """Test /auth/me endpoint with mocked user authentication."""
    # Create a mock user
    mock_user = UserInfo(
        id="test-user-id",
        email="test@example.com",
        aud="authenticated",
        exp=9999999999,
        sub="test-user-id",
        user_metadata={"name": "Test User"}
    )
    
    # Override the dependency for this test
    def override_get_current_user():
        return mock_user
    
    app.dependency_overrides[get_current_user] = override_get_current_user
    
    try:
        response = client.get("/auth/me")
        assert response.status_code == 200
        data = response.json()
        assert data["authenticated"] is True
        assert data["user"]["id"] == "test-user-id"
        assert data["user"]["email"] == "test@example.com"
    finally:
        # Clean up the override
        app.dependency_overrides = {}

def test_plans_endpoint_with_mock_user() -> None:
    """Test /api/plans endpoint with mocked user authentication."""
    from auth import get_current_user
    from main import PLANS_DB
    PLANS_DB.clear()
    mock_user = UserInfo(
        id="test-user-id",
        email="test@example.com",
        aud="authenticated",
        exp=9999999999,
        sub="test-user-id"
    )
    def override_get_current_user():
        return mock_user
    app.dependency_overrides[get_current_user] = override_get_current_user
    try:
        # Add a plan for this user
        PLANS_DB.append({
            "id": "plan-1",
            "user_id": "test-user-id",
            "title": "Test Plan",
            "description": "Test Desc",
            "schedule": {"monday": "study"}
        })
        response = client.get("/api/plans")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["user_id"] == "test-user-id"
        assert data[0]["title"] == "Test Plan"
    finally:
        app.dependency_overrides = {}
        PLANS_DB.clear()

def test_create_plan_endpoint_with_mock_user() -> None:
    """Test POST /api/plans endpoint with mocked user authentication."""
    from auth import get_current_user
    from main import PLANS_DB
    PLANS_DB.clear()
    mock_user = UserInfo(
        id="test-user-id",
        email="test@example.com",
        aud="authenticated",
        exp=9999999999,
        sub="test-user-id"
    )
    def override_get_current_user():
        return mock_user
    app.dependency_overrides[get_current_user] = override_get_current_user
    try:
        plan_data = {"title": "Test Plan", "description": "Test Description", "schedule": {"monday": "study"}}
        response = client.post("/api/plans", json=plan_data)
        assert response.status_code == 200
        plan = response.json()
        assert plan["user_id"] == "test-user-id"
        assert plan["title"] == "Test Plan"
        assert plan["schedule"] == {"monday": "study"}
    finally:
        app.dependency_overrides = {}
        PLANS_DB.clear()

def test_create_and_list_plans_with_mock_user() -> None:
    """Test creating and listing plans for the authenticated user."""
    from auth import get_current_user
    from main import PLANS_DB
    PLANS_DB.clear()
    mock_user = UserInfo(
        id="test-user-id",
        email="test@example.com",
        aud="authenticated",
        exp=9999999999,
        sub="test-user-id"
    )
    def override_get_current_user():
        return mock_user
    app.dependency_overrides[get_current_user] = override_get_current_user
    try:
        # Create a plan
        plan_data = {"title": "Math Plan", "description": "Algebra", "schedule": {"monday": "study"}}
        response = client.post("/api/plans", json=plan_data)
        assert response.status_code == 200
        plan = response.json()
        assert plan["title"] == "Math Plan"
        assert plan["user_id"] == "test-user-id"
        # List plans
        response = client.get("/api/plans")
        assert response.status_code == 200
        plans = response.json()
        assert isinstance(plans, list)
        assert len(plans) == 1
        assert plans[0]["title"] == "Math Plan"
    finally:
        app.dependency_overrides = {}
        PLANS_DB.clear()

def test_streaks_endpoint_with_mock_user() -> None:
    """Test /api/streaks endpoint with mocked user authentication."""
    # Create a mock user
    mock_user = UserInfo(
        id="test-user-id",
        email="test@example.com",
        aud="authenticated",
        exp=9999999999,
        sub="test-user-id"
    )
    
    # Override the dependency for this test
    def override_get_current_user():
        return mock_user
    
    app.dependency_overrides[get_current_user] = override_get_current_user
    
    try:
        response = client.get("/api/streaks")
        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == "test-user-id"
        assert "streaks" in data
        assert "message" in data
    finally:
        # Clean up the override
        app.dependency_overrides = {}