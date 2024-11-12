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
                            desc = input('Digite a nova descricao: ')
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

#Teste

while True:
    try:
        print("Olá, aqui você poderá usar nosso sistema de cadastro de servicos. O que gostaria de fazer?")
        menu = int(input('(1)Criar um servico\n(2)Listar um servico ja criado\n(3)Alterar um servico\n(3)Excluir um servico\n(7)Sair\n'))
        match menu:
            case 1:
                nome = input("Escreva o nome do servico:\n")
                desc = input("Escreva uma descricao para o servico:\n")
                duracao = input("Escreva a duracao do servico:\n")
                adicionar_servicos(nome, desc, duracao)
            case 2:
                print("\t\tComo você gostaria de listar o servico?")
                listagem = int(input('\t\t(1)Listar por nome\n\t\t(2)Listar por descricao\n\t\t(3)Listar por duracao\n\t\t(4)Busca por ID\n\t\t(7)Sair\n'))
                match listagem:
                    case 1:
                        print('\t\t',listar_por_nome())
                    case 2:
                        print('\t\t',listar_por_descricao())
                    case 3:
                        print('\t\t',listar_por_duracao())
                    case 4:
                        id = input("\t\tEscreva o id do servico desejado:")
                        print('\t\t',achar_por_id(id))
                    case 7:
                        break
                    case __:
                        print('\t\tOpção invalida.\nDigite uma opção valida: ')
            case 3:
                 id = input("Escreva o id do servico que vc deseja alterar:")
                 atualizar_servicos(id)
            case 4:
                 id = input("Escreva o id do servico que vc deseja Excluir:")
                 remover_servicos(id)
            case 7:
                break
            case __:
                print('Opção invalida.\nDigite uma opção valida: ')
    except ValueError:
        print('Entrada invalida.\nDigite uma opção valida: ')