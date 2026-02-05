from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from src.routes import (
    people_finder_route,
    people_register_route,
    auth_route
)

app = FastAPI()

app.include_router(people_finder_route.router)
app.include_router(people_register_route.router)
app.include_router(auth_route.router)

@app.get("/health")
def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)