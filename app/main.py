from fastapi import FastAPI
from app.database import engine, Base

# IMPORTA EL MODELO
from app.models import product  
from app.routes import product as product_routes

app = FastAPI(title="Verdana Backend")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(product_routes.router)

@app.get("/")
def root():
    return {"message": "Backend working fine!"}
