import json
import os
import pyautogui

products_file = os.path.join(os.path.dirname(__file__), "products.json")

if not os.path.exists(products_file):
    with open(products_file, 'w') as file:
        json.dump({}, file, indent=4)

class Product:
    def __init__(self, product_id, name, description, value, available):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.value = value
        self.available = available
        
    @staticmethod
    def load_file():
        with open(products_file, 'r') as file:
            return json.load(file)
        
    @staticmethod
    def generate_id():
        data = Product.load_file()
        if data:
            max_id = max(int(product_id) for product_id in data.keys())
            return str(max_id + 1)
        return "1"

    @classmethod
    def menu(cls):
        while True:
            option = pyautogui.prompt(
                text= "Escolha uma opção:\n1. Adicionar Produto\n0. Sair",
                title= "Menu de Produtos"
            )
            match(option):
                case "1":
                    product_id = cls.generate_id()
                    name = pyautogui.prompt("Nome do produto: ")
                    description = pyautogui.prompt("Descrição do produto: ")
                    value = pyautogui.prompt("Valor do produto: ")
                    available = pyautogui.prompt("Produto disponível? (True/False)")

                    try:
                        value = float(value)
                        available = available.lower() == 'true'
                    except ValueError:
                        pyautogui.alert("Entrada inválida para valor ou disponibilidade!")
                        continue
                    cls.add_product(product_id, name, description, value, available)
                case "0":
                    pyautogui.alert("Encerrando o programa.")
                    break
                case _:
                    pyautogui.alert("Opção inválida. Tente novamente.")
                    continue
       
    @classmethod    
    def add_product(cls, product_id, name, description, value, available):
        data = cls.load_file()
        data[product_id] = {
            'name': name,
            'description': description,
            'value': value,
            'available': available
        }
        with open(products_file, 'w') as file:
            json.dump(data, file, indent=4)
        pyautogui.alert(f"Produto '{name}' adicionado com sucesso!")

if __name__ == "__main__":
    Product.menu()