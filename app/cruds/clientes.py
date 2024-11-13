import os
import json
from app.models.clientes import ClienteModel
from app.config import DATA_PATHS


arquivo_clientes = DATA_PATHS['clientes']

def carregar_clientes():
    if os.path.exists(arquivo_clientes) and os.path.getsize(arquivo_clientes) > 0:
        with open(arquivo_clientes, 'r') as file:
            return json.load(file)
    return {}

def salvar_cliente(clientes):
    with open(arquivo_clientes, 'w') as file:
        json.dump(clientes, file, indent=4)

def gerar_id_cliente(clientes):
    if clientes:
        max_id = max(int(id_cliente) for id_cliente in clientes.keys())
        return str(max_id + 1)
    return "1"

def adicionar_cliente(cliente_data: ClienteModel):
    clientes = carregar_clientes()
    id_cliente = gerar_id_cliente(clientes)
    clientes[id_cliente] = cliente_data.dict()
    salvar_cliente(clientes)
    return id_cliente

def listar_clientes():
    return carregar_clientes()

def atualizar_cliente(id_cliente: str, cliente_data: ClienteModel):
    clientes = carregar_clientes()
    if id_cliente in clientes:
        clientes[id_cliente] = cliente_data.dict()
        salvar_cliente(clientes)
        return True
    return False

def deletar_cliente(id_cliente: str):
    clientes = carregar_clientes()
    if id_cliente in clientes:
        del clientes[id_cliente]
        salvar_cliente(clientes)
        return True
    return False
