from fastapi import APIRouter, HTTPException
from app.models.products import ProductModel, ProductUpdateModel
from app.cruds.products import Product

router = APIRouter()

@router.post("/products/", response_model=ProductModel)
def create_product(product: ProductModel):
    return Product.add_product(product.name, product.description, product.value, product.available)

@router.put("/products/{product_id}", response_model=ProductModel)
def update_product(product_id: str, update: ProductUpdateModel):
    return Product.update_product(product_id, update.field, update.value)
