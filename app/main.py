from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import TaskCreate, TaskResponse
from app.database import engine, SessionLocal
from app import models

# Esto crea el archivo tasks.db y sus tablas automáticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskFlow API",
    description="REST API for managing projects and tasks.",
    version="0.1.0"
)

# --- INYECCIÓN DE DEPENDENCIAS ---
# Esta función abre la base de datos cuando llega una petición y la cierra al terminar.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "TaskFlow API is running", "version": "0.1.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# --- ENDPOINTS CONECTADOS A SQLITE ---

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Convertimos el esquema de entrada a un modelo de base de datos
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit() # Guardamos los cambios en disco
    db.refresh(db_task)
    return db_task

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    # Trae todas las tareas de la base de datos
    tasks = db.query(models.Task).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    # Busca una tarea específica por su ID
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    # Busca y elimina
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit() # Guardamos la eliminación en disco
    return {"message": "Task deleted"}