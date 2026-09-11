from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_api_rejects_empty_url():
    client = app.test_client()
    response = client.get("/api/check")
    assert response.status_code == 400
    assert "error" in response.get_json()
