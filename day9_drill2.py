from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo/{text}")
def echo(text: str):
    return {
        "You Entered": text
    }

@app.get("/greet")
def greet(name: str):
    return {
        "message": f"Hello {name}, Welcome to FastAPI!"
    }