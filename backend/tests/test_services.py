import json
import os
import pytest
from app import services

@pytest.fixture
def temp_data_dir(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir

def test_check_dataset_exists(temp_data_dir):
    # Set up test paths
    services.datafolder = str(temp_data_dir)
    services.datasource = str(temp_data_dir / "users.json")
    
    # Test creation of data file
    services.check_dataset_exists()
    assert os.path.exists(services.datafolder)
    assert os.path.exists(services.datasource)

def test_read_usersdata(temp_data_dir):
    # Set up test paths
    services.datafolder = str(temp_data_dir)
    services.datasource = str(temp_data_dir / "users.json")
    
    # Create test data
    test_data = {"data": [{"first_name": "Test", "last_name": "User", "age": 25}]}
    with open(services.datasource, "w") as f:
        json.dump(test_data, f)
    
    # Test reading data
    result = services.read_usersdata()
    assert result == test_data
    assert "data" in result
    assert len(result["data"]) == 1

def test_add_userdata(temp_data_dir):
    # Set up test paths
    services.datafolder = str(temp_data_dir)
    services.datasource = str(temp_data_dir / "users.json")
    
    # Initialize empty data file
    services.check_dataset_exists()
    
    # Test adding user
    test_user = {"first_name": "New", "last_name": "User", "age": 30}
    services.add_userdata(test_user)
    
    # Verify user was added
    with open(services.datasource, "r") as f:
        data = json.load(f)
    assert "data" in data
    assert len(data["data"]) == 1
    assert data["data"][0] == test_user

def test_add_multiple_users(temp_data_dir):
    # Set up test paths
    services.datafolder = str(temp_data_dir)
    services.datasource = str(temp_data_dir / "users.json")
    
    # Initialize empty data file
    services.check_dataset_exists()
    
    # Add multiple users
    users = [
        {"first_name": "User1", "last_name": "Test", "age": 20},
        {"first_name": "User2", "last_name": "Test", "age": 25}
    ]
    
    for user in users:
        services.add_userdata(user)
    
    # Verify all users were added
    result = services.read_usersdata()
    assert len(result["data"]) == 2
    assert all(user in result["data"] for user in users)