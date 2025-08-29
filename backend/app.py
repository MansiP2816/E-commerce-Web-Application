from fastapi import FastAPI

app = FastAPI()

# Sample products
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 600}
]

@app.get("/")
def home():
    return {"message": "E-commerce API is running"}

@app.get("/products")
def get_products():
    return products
