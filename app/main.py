from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.settings import settings

app = FastAPI(title=settings.APP_NAME)

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