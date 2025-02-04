from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
  return {"message" : "Hello, FastAPI"}

@app.get("/read")
def read():
  return {"read" : "Hello, FastAPI"}