"""This module defines a basic FastAPI app that returns 'Hello, World!'."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Root endpoint that returns a Hello World message."""
    return {"message": "Hello, World!"}
