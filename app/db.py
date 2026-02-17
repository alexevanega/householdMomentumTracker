from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import settings

#SQLite needs this flag for multi-threaded access in typical FastAPI usage.
connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():

    """
    FastAPI dependency that yields a DB session and guarantees cleanup.
    Models are NOT created in phase 0.

    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()