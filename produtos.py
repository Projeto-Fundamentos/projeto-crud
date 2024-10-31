import json
import os

products_file = os.path.join(os.path.dirname(__file__), "products.json")

if not os.path.exists(products_file):
    with open(products_file, 'w') as file:
        json.dump({}, file, indent=4)

def load_file():
    