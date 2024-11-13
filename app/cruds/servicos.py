import json
import os
from app.config import DATA_PATHS
from app.models.servicos import Servico

services = DATA_PATHS['servicos']

def carregar_servicos():
    if not os.path.exists(services):
        with open(services, 'w') as f:
            json.dump({}, f, indent=4)
    with open(services, 'r') as f:
        return json.load(f)

def gerar_id():
    data = carregar_servicos()
    if data:
        maxId = max(int(servicoId) for servicoId in data.keys())
        return str(maxId + 1)
    return "1"

def adicionar_servicos(nome: str, descricao: str, duracao: int):
    lista_servicos = carregar_servicos()
    novo_servico = Servico(nome=nome, descricao=descricao, duracao=duracao)
    novo_id = gerar_id()
    novo_servico.servico_id = novo_id
    lista_servicos[novo_id] = {
        'nome': nome,
        'descricao': descricao,
        'duracao': duracao
    }
    with open(services, 'w') as f:
        json.dump(lista_servicos, f, indent=4)

def listar_por_nome():
    lista_servicos = carregar_servicos()
    lista_por_nome = dict(sorted(lista_servicos.items(), key=lambda servico: servico[1]['nome']))
    return lista_por_nome

def listar_por_descricao():
    lista_servicos = carregar_servicos()
    lista_por_descricao = dict(sorted(lista_servicos.items(), key=lambda servico: servico[1]['descricao']))
    return lista_por_descricao

def listar_por_duracao():
    lista_servicos = carregar_servicos()
    lista_por_duracao = dict(sorted(lista_servicos.items(), key=lambda servico: int(servico[1]['duracao'])))
    return lista_por_duracao

def achar_por_id(id: str):
    lista_servicos = carregar_servicos()
    return lista_servicos.get(id, None)

def atualizar_servicos(id: str, nome: str, descricao: str, duracao: int):
    lista_servicos = carregar_servicos()
    servico = lista_servicos.get(id)
    if servico:
        lista_servicos[id]['nome'] = nome
        lista_servicos[id]['descricao'] = descricao
        lista_servicos[id]['duracao'] = duracao
        with open(services, 'w') as f:
            json.dump(lista_servicos, f, indent=4)
        return True
    return False

def remover_servicos(id: str):
    lista_servicos = carregar_servicos()
    if id in lista_servicos:
        del lista_servicos[id]
        with open(services, 'w') as f:
            json.dump(lista_servicos, f, indent=4)
        return True
    return False
