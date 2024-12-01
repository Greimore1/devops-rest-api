from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/", 
        json={"name": "Test Item", "price": 99.99}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"

def test_list_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item():
    # First create an item
    create_response = client.post(
        "/items/", 
        json={"name": "Retrieve Item", "price": 49.99}
    )
    item_id = create_response.json()["id"]
    
    # Then retrieve it
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Retrieve Item"
