import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .exif import read_exif
from .ela import run_ela

app = FastAPI(
    title="Ghost Image Forensics API",
    description="Moteur d'Analyse EXIF & Détection d'Altérations ELA",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil de forensics d'images
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Ghost API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Ghost", "version": "1.0.0"}

@app.get("/api/v1/exif", response_model=ResultContract)
def get_exif(image_path: str = Query("sample.jpg")):
    return read_exif(image_path)

@app.get("/api/v1/ela")
def get_ela(image_path: str = Query("sample.jpg")):
    return run_ela(image_path)
