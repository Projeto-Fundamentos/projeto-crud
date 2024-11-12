import json
import os

services = os.path.join(os.path.dirname(__file__), 'services.json')

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
        return str(maxId+1)
    return "1"

class Servico:
    def __init__(self, nome, descricao, duracao):
        self.servico_id = gerar_id()
        self.nome = nome
        self.descricao = descricao 
        self.duracao = duracao

#CREATE    
def adicionar_servicos(nome, descricao, duracao):
    lista_servicos = carregar_servicos()
    novo_servico = Servico(nome, descricao, duracao)
    lista_servicos[novo_servico.servico_id] = {
        'nome': nome,
        'descricao': descricao,
        'duracao': duracao
    }
    with open(services, 'w') as f:
        json.dump(lista_servicos, f, indent=4)

#adicionar_servicos('tosa', 'custa tempo', 10)
#adicionar_servicos('banho', 'cheiro bom', 5)
#adicionar_servicos('adestrar', 'pet calmo', 500000)

#READ
##ordenado
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

def achar_por_id(id):
    lista_servicos = carregar_servicos()
    for servico_id, desc in lista_servicos.items():
        if(servico_id == id):
            return desc

#print(listar_por_nome())

#print(listar_por_descricao())

#print(listar_por_duracao())

#print(achar_por_id('2'))




#UPDATE
def atualizar_servicos(id):
    lista_servicos = carregar_servicos()
    for servico_id, desc in lista_servicos.items():
        if servico_id == id:
            while True:
                try:
                    escolha = int(input('(1) Alterar nome\n(2)Alterar descricao\n(3)Alterar duracao\n(7)Sair\n'))
                    match escolha:
                        case 1:
                            nome = input('Digite o novo nome: ')
                            lista_servicos[servico_id]['nome'] = nome
                        case 2:
                            cor = input('Digite a nova descricao: ')
                            lista_servicos[servico_id]['descricao'] = desc
                        case 3:
                            duracao = input('Digite a nova duracao: ')
                            lista_servicos[servico_id]['duracao'] = duracao
                        case 7:
                            break
                        case __:
                            print('Opção invalida.\nDigite uma opção valida: ')
                except ValueError:
                    print('Entrada invalida.\nDigite uma opção valida: ')
        print('Campo atualizado com sucesso!')
        with open(services, 'w') as f:
            json.dump(lista_servicos, f, indent=4)


#atualizar_servicos('2')
#print(listar_por_nome())

#DELETE
def remover_servicos(id):
    lista_servico = carregar_servicos()
    servico = False
    for servico_id, desc in lista_servico.items():
        if id == servico_id:
            servico = True
            del lista_servico[servico_id]
            with open(services, 'w') as f:
                json.dump(lista_servico, f, indent=4)
            print('Servico removido!')
            break 
    if servico == False:
        print('Servico não encontrado')

#remover_servicos('2')