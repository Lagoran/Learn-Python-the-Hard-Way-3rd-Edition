from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """Test that root endpoint returns Hello world! message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_read_html():
    """Test that HTML endpoint returns Hello world! as HTML"""
    response = client.get("/html")
    assert response.status_code == 200
    assert "Hello world!" in response.text
    assert "<html>" in response.text
