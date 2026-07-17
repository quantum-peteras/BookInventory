from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mission Impossible: Book Inventory",
    version="1.0.0",
    description="Mission impossible: Book Inventory"
)

app.include_router(
    books.router
)

@app.get("/")
def home():
    return {
        "message":
        "Welcome to the Peter Turkson Asamoah Book Inventory"
    }