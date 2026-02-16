from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.settings import settings

app = FastAPI(title=settings.APP_NAME)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/api/health")
def health():
    return {"status":"ok"}