from fastapi import FastAPI
from app.settings import settings

app = FastAPI(title=settings.APP_NAME)

@app.get("/api/health")
def health():
    return {"status":"ok"}