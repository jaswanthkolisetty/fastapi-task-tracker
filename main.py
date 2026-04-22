from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI Task Tracker is running"}


@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {"id": 1, "title": "Learn Git basics", "done": False},
            {"id": 2, "title": "Push first commit", "done": False},
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}