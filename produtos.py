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
                text= "Escolha uma opção:\n1. Adicionar Produto\n3. Atualizar Produto\n0. Sair",
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
                        pyautogui.alert("Entrada inválida para valor ou disponibilidade.")
                        continue
                    cls.add_product(product_id, name, description, value, available)
                case "2":
                    # LÓGICA PARA EXIBIR PRODUTOS
                    pass
                case "3":
                    data = cls.load_file()
                    update_id = pyautogui.prompt(
                        text= "Insira o id do produto a ser atualizado"
                    )
                    if not update_id in data.keys():
                        pyautogui.alert("Id inválido.")
                        continue
                    update_option = pyautogui.prompt(
                        text= "Escolha a opção que deseja atualizar:\n1.Nome\n2.Descrição\n3.Valor\n4.Disponibildade\n0. Voltar ao menu principal"
                    )
                    new_data = []
                    match(update_option):
                        case "1":
                            new_data.append("name")
                            new_data.append(pyautogui.prompt("Insira o novo nome do produto: "))
                        case "2":
                            new_data.append("description")
                            new_data.append(pyautogui.prompt("Insira a nova descrição do produto: "))
                        case "3":
                            new_data.append("value")
                            try:
                                float(new_data.append(pyautogui.prompt("Insira o novo valor do produto: ")))
                            except TypeError:
                                pyautogui.alert("O valor deve ser um número!")
                        case "4":
                            new_data.append("available")
                            available = pyautogui.prompt("Insira a nova disponibilidade do produto: ")
                            if available.lower() in ['true', 'false']:
                                new_data.append(available.lower())
                            else:
                                pyautogui.alert("Valor inválido! Digite apenas 'true' ou 'false'.")
                        case "0":
                            continue
                        case _:
                            pyautogui.alert("Valor de entrada inválido.")
                            continue
                    if new_data[1].strip():
                        Product.update_product(update_id, new_data)
                    else:
                        print('vazio')
                case "4":
                    # LÓGICA PARA DELETAR PRODUTO
                    pass
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

    @classmethod
    def update_product(cls, product_id, update_list):
        
        data = cls.load_file()
        data[product_id].update({
            update_list[0]: update_list[1]
        })
        with open(products_file, 'w') as file:
            json.dump(data, file, indent=4)
        pyautogui.alert(f"Produto '{product_id}' atualizado com sucesso!")

if __name__ == "__main__":
    Product.menu()