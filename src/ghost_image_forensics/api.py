from fastapi import FastAPI
from .exif import read_exif
from .ela import run_ela

app = FastAPI(title="Ghost Image Forensics API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Ghost"}

@app.get("/api/v1/exif")
def exif(image_path: str):
    return read_exif(image_path)

@app.get("/api/v1/ela")
def ela(image_path: str):
    return run_ela(image_path)
