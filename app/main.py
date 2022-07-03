import uvicorn
from auth import main as auth
from talents import main as talents
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(talents.router)

@app.get("/")
def read_root(username: str = Depends(auth.authenticate)):
    return { "Result": "Hello Everyone, This is Archipel Cognitive Python Backend" }

@app.get("/users/me")
def read_current_user(username: str = Depends(auth.authenticate)):
    return {"username": username}

if __name__ == '__main__':
    uvicorn.run("main:app", host = '0.0.0.0', port = 1005, reload = True)