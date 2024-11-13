import json
import os

from fastapi import HTTPException
from app.config import DATA_PATHS

products_file = DATA_PATHS['produtos']

if not os.path.exists(products_file):
    with open(products_file, 'w') as file:
        json.dump({}, file, indent=4)

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
    def add_product(name, description, value, available):
        product_id = Product.generate_id()
        data = Product.load_file()
        product_data = {
            'name': name,
            'description': description,
            'value': value,
            'available': available
        }
        data[product_id] = product_data
        Product.save_file(data)
        return {"id": product_id, **product_data}

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
   
    @staticmethod
    def get_all_products():
        data = Product.load_file()
        return {"products": data}

    @staticmethod
    def get_single_product(product_id):
        data = Product.load_file()
        if product_id not in data:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return {"id": product_id, **data[product_id]}

    @staticmethod
    def delete_product(product_id):
        data = Product.load_file()
        if product_id not in data:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        deleted_product = data.pop(product_id)
        Product.save_file(data)
        return {"message": f"Produto {product_id} removido com sucesso", "deleted_product": deleted_product}