from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, properties, tenants, agreements, payments

app = FastAPI()

# Enable CORS for local static file loading and development origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(properties.router, prefix="/properties", tags=["Properties"])
app.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
app.include_router(agreements.router, prefix="/agreements", tags=["Agreements"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])


@app.get("/")
def home():
    return {"message": "Property Rental API Running"}