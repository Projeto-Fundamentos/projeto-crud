from pydantic import BaseModel

class ProductModel(BaseModel):
    name: str
    description: str
    value: float
    available: bool

class ProductUpdateModel(BaseModel):
    field: str
    value: str