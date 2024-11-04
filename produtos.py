import json
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

products_file = os.path.join(os.path.dirname(__file__), "products.json")

if not os.path.exists(products_file):
    with open(products_file, 'w') as file:
        json.dump({}, file, indent=4)

app = FastAPI()

class ProductModel(BaseModel):
    name: str
    description: str
    value: float
    available: bool

class ProductUpdateModel(BaseModel):
    field: str
    value: str

class Product:        
    @staticmethod
    def load_file():
        with open(products_file, 'r') as file:
            return json.load(file)
    @staticmethod
    def save_file(data):
        with open(products_file, 'w') as file:
            json.dump(data, file, indent=4)
        
    @staticmethod
    def generate_id():
        data = Product.load_file()
        if data:
            max_id = max(int(product_id) for product_id in data.keys())
            return str(max_id + 1)
        return "1"
       
    @staticmethod    
    def add_product(product_id, name, description, value, available):
        data = Product.load_file()
        data[product_id] = {
            'name': name,
            'description': description,
            'value': value,
            'available': available
        }
        Product.save_file(data)

    @staticmethod
    def update_product(product_id, field, value):
        data = Product.load_file()
        if product_id not in data:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        if field in data[product_id]:
            if field == "value":
                value = float(value)
            elif field == "available":
                value = value.lower() == 'true'
            data[product_id][field] = value
            Product.save_file(data)
        else:
            raise HTTPException(status_code=404, detail="Campo inválido para atualizar")

@app.post("/adicionar_produto/")
def add_product(product: ProductModel):
    product_id = Product.generate_id()
    Product.add_product(product_id, product.name, product.description, product.value, product.available)
    return {"message": f"Produto '{product.name}' adicionado com sucesso!", "product_id": product_id}

@app.put("/atualizar_produto/{product_id}")
def update_product(product_id: str, update_data: ProductUpdateModel):
    Product.update_product(product_id, update_data.field, update_data.value)
    return {"message": f"Produto '{product_id}' atualizado com sucesso!"}

@app.get("/listar_produtos/")
def get_products():
    data = Product.load_file()
    return data