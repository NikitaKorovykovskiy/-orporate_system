from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def login(username: str, password: str):
    # Реализация логики аутентификации
    return {"username": username}