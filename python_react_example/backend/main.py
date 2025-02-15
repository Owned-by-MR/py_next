from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import product_routes
from app.database import engine
from app.models.product import ProductDB

# Create database tables
ProductDB.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes.router, prefix="/api/products")
