from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router
from app.config.database import Base, engine
import app.models.user  # wichtig: sorgt dafür, dass das Model registriert wird

app = FastAPI(title="AgentFlow API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "AgentFlow API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth_router)