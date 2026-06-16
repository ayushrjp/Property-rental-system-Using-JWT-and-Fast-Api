from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.api import auth, properties, tenants, agreements, payments

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve index.html at root
@app.get("/")
def serve_index():
    return FileResponse(os.path.join("app/static", "index.html"))

# API routes
app.include_router(auth.router, prefix="/auth")
app.include_router(properties.router, prefix="/properties")
app.include_router(tenants.router, prefix="/tenants")
app.include_router(agreements.router, prefix="/agreements")
app.include_router(payments.router, prefix="/payments")