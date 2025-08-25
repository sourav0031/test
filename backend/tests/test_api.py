import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_fit_score():
    resp = client.post('/fit-score', json={'hoi':0.7,'roi':0.6})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_submit():
    resp = client.post('/submit', json={'hoi':0.7,'roi':0.6})
    assert resp.status_code == 200
    assert '<h1>Top Cities</h1>' in resp.text


def test_submit_pdf():
    resp = client.post('/submit/pdf', json={'hoi':0.7,'roi':0.6})
    assert resp.status_code == 501
