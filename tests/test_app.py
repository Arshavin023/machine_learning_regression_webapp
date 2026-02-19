# test_app.py

import pytest
from src.app import application as app
from unittest.mock import patch


@pytest.fixture
def client():
    """
    Creates a test client for the Flask app.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    """
    Test the homepage route.
    """
    response = client.get("/")
    assert response.status_code == 200


def test_health_route(client):
    """
    Test the health endpoint.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_predict_get(client):
    """
    Test GET request to /predict route.
    """
    response = client.get("/predict")
    assert response.status_code == 200


@patch("src.pipeline.predict_pipeline.PredictPipeline.predict")
def test_predict_post(mock_predict, client):
    """
    Test POST request to /predict route.
    Mocking PredictPipeline to avoid loading actual ML model.
    """

    # Mock prediction result
    mock_predict.return_value = [85.0]

    response = client.post(
        "/predict",
        data={
            "gender": "male",
            "ethnicity": "group A",
            "parental_level_of_education": "bachelor's degree",
            "lunch": "standard",
            "test_preparation_course": "none",
            "reading_score": "72",
            "writing_score": "74",
        },
    )

    assert response.status_code == 200
    assert b"85.0" in response.data
