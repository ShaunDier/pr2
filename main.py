from fastapi import FastAPI

app = FastAPI(title="To-do API, version 0.1.0")
tasks: list[str] = []

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks() -> list[str]:
    return tasks

@app.post("/tasks", status_code=201)
def add_task(title: str) -> list[str]:
    tasks.append(title)
    return tasks