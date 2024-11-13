import json
import os
from app.config import DATA_PATHS
from app.models.funcionarios import Funcionario

arquivo_funcionarios = DATA_PATHS['funcionarios']

def carregar_funcionarios():
    if os.path.exists(arquivo_funcionarios) and os.path.getsize(arquivo_funcionarios) > 0:
        with open(arquivo_funcionarios, 'r') as file:
            return json.load(file)
    else:
        return {}

def salvar_funcionario(funcionarios):
    with open(arquivo_funcionarios, 'w') as file:
        json.dump(funcionarios, file, indent=4)

def gerar_id_funcionario(funcionarios):
    if funcionarios:
        maxId = max(int(id_funcionario) for id_funcionario in funcionarios.keys())
        return str(maxId + 1)
    return "1"

def add_funcionario(funcionario: Funcionario):
    funcionarios = carregar_funcionarios()
    id_funcionario = gerar_id_funcionario(funcionarios)
    funcionarios[id_funcionario] = funcionario.dict()
    salvar_funcionario(funcionarios)

def listar_funcionarios():
    return carregar_funcionarios()

def excluir_funcionario(id_funcionario: str):
    funcionarios = carregar_funcionarios()
    if id_funcionario in funcionarios:
        del funcionarios[id_funcionario]
        salvar_funcionario(funcionarios)
        return True
    return False

def atualizar_funcionario(id_funcionario: str, funcionario: Funcionario):
    funcionarios = carregar_funcionarios()
    if id_funcionario in funcionarios:
        funcionarios[id_funcionario] = funcionario.dict()
        salvar_funcionario(funcionarios)
        return True
    return False
