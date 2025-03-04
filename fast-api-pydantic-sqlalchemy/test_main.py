from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_add_item():
    # Define the item to add
    new_item = {
       
        "name": "Helo",
        "description": "This is a sample item222"
    }

    # Add the item
    response = client.post("/items/", json=new_item)

    # Assert the response
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == "Helo"
    assert response_json["description"] == "This is a sample item222"
    assert 'id' in response_json
    
    
    