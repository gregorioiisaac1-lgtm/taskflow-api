from fastapi import FastAPI, HTTPException
from app.schemas import TaskCreate, TaskResponse

app = FastAPI(
    title="TaskFlow API",
    description="REST API for managing projects and tasks.",
    version="0.1.0"
)

# Base de datos temporal en memoria
tasks: list[dict] = []

@app.get("/")
def root():
    return {
        "message": "TaskFlow API is running",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

# --- NUEVOS ENDPOINTS PARA TAREAS ---

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    tasks.append(new_task)
    return new_task

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return {"message": "Task deleted"}
    
    raise HTTPException(
        status_code=404, 
        detail="Task not found"
    )