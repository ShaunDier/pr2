from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

def setup_function():
    main.tasks.clear()

def test_add_task_unit():
    assert main.add_task("Buy milk") == ["Buy milk"]
    assert main.list_tasks() == ["Buy milk"]

def test_add_task_api():
    response = client.post("/tasks", params={"title": "Buy milk"})

    assert response.status_code == 201
    assert client.get("/tasks").json() == ["Buy milk"]