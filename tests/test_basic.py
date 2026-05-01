from app.main import app

def test_borrow_and_return():
    client = app.test_client()

    client.post("/books", json={"title": "AI", "author": "X"})
    res = client.post("/borrow", json={"book_id": 1, "user": "A"})
    assert res.status_code == 200

    res = client.post("/return", json={"book_id": 1})
    assert "fine" in res.get_json()