import json
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import services

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_test_data(tmp_path):
    # Create a temporary data directory
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    test_file = data_dir / "users.json"
    
    # Mock the data file path
    services.datafolder = str(data_dir)
    services.datasource = str(test_file)
    
    # Initialize empty data
    with open(test_file, "w") as f:
        json.dump({"data": []}, f)
    
    yield
    
    # Cleanup
    if test_file.exists():
        test_file.unlink()
    if data_dir.exists():
        data_dir.rmdir()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_user():
    test_user = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30
    }
    response = client.post("/users", json=test_user)
    assert response.status_code == 200
    assert response.json() == {"success": True}

def test_get_users():
    # First create a test user
    test_user = {
        "first_name": "Jane",
        "last_name": "Doe",
        "age": 25
    }
    client.post("/users", json=test_user)
    
    # Then get all users
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert "data" in users
    assert len(users["data"]) > 0
    assert any(user["first_name"] == "Jane" for user in users["data"])

def test_create_invalid_user():
    test_user = {
        "first_name": "John",
        "last_name": "Doe",
        "age": "invalid"  # age should be an integer
    }
    response = client.post("/users", json=test_user)
    assert response.status_code == 422  # Validation error

def test_create_user_missing_fields():
    test_user = {
        "first_name": "John"
        # missing last_name and age
    }
    response = client.post("/users", json=test_user)
    assert response.status_code == 422  # Validation error