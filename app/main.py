from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="DevOps Learning REST API",
    description="A simple REST API project for DevOps engineers to learn and practice",
    version="0.1.0"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
