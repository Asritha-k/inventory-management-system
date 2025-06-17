from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={"name": "Keyboard", "quantity": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Keyboard"
    assert data["quantity"] == 10
    assert "id" in data

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_item():
    # First create item
    response = client.post("/items", json={"name": "Mouse", "quantity": 5})
    item_id = response.json()["id"]

    # Update quantity
    response = client.put(f"/items/{item_id}?quantity=15")
    assert response.status_code == 200
    assert response.json()["quantity"] == 15

def test_delete_item():
    # First create item
    response = client.post("/items", json={"name": "Monitor", "quantity": 2})
    item_id = response.json()["id"]

    # Delete it
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
