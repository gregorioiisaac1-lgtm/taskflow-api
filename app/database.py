from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Crea la ruta al archivo de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# connect_args es necesario solo para SQLite en FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()