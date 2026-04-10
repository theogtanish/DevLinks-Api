from fastapi import FastAPI
from app.database import engine, Base
from app.routers import links_router
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevLinks API")

app.include_router(links_router)

@app.get("/")
def root():
    return {"status": "ok", "message": "DevLinks API is running"}