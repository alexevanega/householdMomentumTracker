from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.settings import settings
from app.db import init_db, get_db
from app.models.user import User
from app.models.task import Task
from app.models.daily_win import DailyWin
from app.models.enums import TaskDomain, TaskEffort, TaskStatus

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (nothing yet)

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": settings.APP_NAME,
            "app_name": settings.APP_NAME
        }
    )

@app.get("/api/health")
def health():
    return {"status":"ok"}

# DEV ONLY: Remove or disable /api/dev/* endpoints outside local development (Phase 7+)
@app.post("/api/dev/seed")
def seed_data(db: Session = Depends(get_db)):
    user1 = User(name="Peter", role="Admin")
    user2 = User(name="Yij", role="Member")

    task1 = Task(
        title="Take out trash",
        domain=TaskDomain.CHORES.value,
        effort=TaskEffort.TINY.value,
        status=TaskStatus.BACKLOG.value,
        definition_of_done="Trash bins emptied and bags replaced",
        materials_needed="Trash bags"
    )

    task2 = Task(
        title="Pay electric bill",
        domain=TaskDomain.BILLS.value,
        effort=TaskEffort.SMALL.value,
        status=TaskStatus.BACKLOG.value,
        definition_of_done="Payment confirmation recieved",
        materials_needed="Credit Card, Bill"
    )

    db.add_all([user1, user2, task1, task2])
    db.commit()

    return {"message": "Seeded dev data"}

@app.get("/api/dev/status")
def dev_status(db: Session = Depends(get_db)):
    return {
        "users": db.query(User).count(),
        "tasks": db.query(Task).count(),
        "daily_wins": db.query(DailyWin).count()
    }