from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health", response_class=JSONResponse)
def health() -> dict:
    """Health check endpoint for API service."""
    return {"status": "ok"}