import json
import os

pets = os.path.join(os.path.dirname(__file__), 'pets.json')

def carregar_pets():
    if not os.path.exists(pets):
        with open(pets, 'w') as f:
            json.dump({}, f, indent=4)
    with open(pets, 'r') as f:
        return json.load(f)

def gerar_id():
    data = carregar_pets()
    if data:
        maxId = max(int(petId) for petId in data.keys())
        return str(maxId+1)
    return "1"

class Pet:
    def __init__(self, nome, idade, raca, cor):
        self.pet_id = gerar_id()
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
        self.obs = ""
        self.adotado = 0

#CREATE
def adicionar_pet(nome, idade, raca, cor):
    lista_pet = carregar_pets()
    novo_pet = Pet(nome, idade, raca, cor)
    lista_pet[novo_pet.pet_id] = {
        'nome': novo_pet.nome,
        'idade': novo_pet.idade,
        'raca': novo_pet.raca,
        'cor': novo_pet.cor,
        'obs': novo_pet.obs,
        'adotado': novo_pet.adotado
    }
    with open(pets, 'w') as f:
        json.dump(lista_pet, f, indent=4)

#READ
def listar_por_idade():
    lista_pets = carregar_pets()
    lista_por_idade = dict(sorted(lista_pets.items(), key=lambda pet: int(pet[1]['idade'])))
    return lista_por_idade

def listar_por_raca():
    lista_pets = carregar_pets()
    lista_por_raca = dict(sorted(lista_pets.items(), key = lambda pet: pet[1]['raca']))
    return lista_por_raca

def achar_por_id(id):
    lista_pets = carregar_pets()
    for pet_id, desc in lista_pets.items():
        if(pet_id == id):
            return desc

#UPDATE
def atualizar_pet(id):
    lista_pets = carregar_pets()
    for pet_id, desc in lista_pets.items():
        if pet_id == id:
            while True:
                try:
                    escolha = int(input('(1) Alterar nome\n(2)Alterar cor\n(3)Alterar raça\n(4)Alterar idade\n(5)Adicionar observação\n(6)Alterar adoção\n(7)Sair\n'))
                    match escolha:
                        case 1:
                            nome = input('Digite o novo nome: ')
                            lista_pets[pet_id]['nome'] = nome
                        case 2:
                            cor = input('Digite a nova cor: ')
                            lista_pets[pet_id]['cor'] = cor
                        case 3:
                            raca = input('Digite a nova raca: ')
                            lista_pets[pet_id]['raca'] = raca
                        case 4:
                            idade = input('Digite a nova idade: ')
                            lista_pets[pet_id]['idade'] = idade
                        case 5:
                            obs = input('Digite a observação: ')
                            lista_pets[pet_id]['obs'] = obs
                        case 6:
                            adotado = input('Pet adotado?\n(1)Sim\n(0)Não:\n ')
                            lista_pets[pet_id]['adotado'] = adotado
                        case 7:
                            break
                        case __:
                            print('Opção invalida.\nDigite uma opção valida: ')
                except ValueError:
                    print('Entrada invalida.\nDigite uma opção valida: ')
        print('Campo atualizado com sucesso!')
        with open(pets, 'w') as f:
            json.dump(lista_pets, f, indent=4)

#DELETE
def remover_pet(id):
    lista_pets = carregar_pets()
    pet = False
    for pet_id, desc in lista_pets.items():
        if id == pet_id:
            pet = True
            del lista_pets[pet_id]
            with open(pets, 'w') as f:
                json.dump(lista_pets, f, indent=4)
            print('Pet removido!')
            break 
    if pet == False:
        print('Pet não encontrado')