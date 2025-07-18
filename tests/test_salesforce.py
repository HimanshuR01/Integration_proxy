from fastapi.testclient import TestClient
from main import app

Client = TestClient(app)

def test_saleforce_integration():
    response = Client.post(
        "/integration/salesforce",
        json={
            "action": "create_lead",
            "parameters": {"name": "Test Account"}
        },
        headers={"X-API-Key": "valid_api_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "Salesforce action" in data["data"]["message"]