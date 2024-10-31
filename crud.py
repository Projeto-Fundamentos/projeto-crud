import json
import os
import uuid

pets = os.path.join(os.path.dirname(__file__), 'pets.json')

def carregar_pet():
    if not os.path.exists(pets):
        with open(pets, 'w') as f:
            json.dump([], f, indent=4)
    with open(pets, 'r') as f:
        return json.load(f)

def gerar_id():
    return str(uuid.uuid4())
    
#CREATE    
def adicionar_pet(nome, idade, raca, cor, obs = "", adotado = 0):
    pet = {
        "numid": gerar_id(),
        "nome": nome,
        "idade": idade,
        "raca": raca,
        "cor": cor,
        "obs": obs,
        "adotado": adotado
    }
    novo_pet = carregar_pet()
    novo_pet.append(pet)
    with open(pets, 'w') as f:
        json.dump(novo_pet, f, indent=4)

#READ
def listar_pets():
    pets = carregar_pet()
    opcao = int(input('(1) Listar pet por idade.\n(2) Listar pet por raça.\n(3) Achar pet pelo nome.\n'))
    match opcao:
        case 1:
            pets_por_idade = sorted(pets, key=lambda pet: int(pet['idade']))
            for key in pets_por_idade:
                print('-'*150)
                print(key)
            print('-'*150)
            return pets_por_idade
        case 2:
            pets_por_raca = sorted(pets, key=lambda pet: pet['raca'])
            for key in pets_por_raca:
                print('-'*150)
                print(key)
            print('-'*150)
        case 3:
            entrada = input('Digite o nome ou ID do pet: ')
            for key in pets:
                if entrada == key['nome'] or entrada == key['numid']:
                    print(f'Nome: {key['nome']}\nIdade: {key['idade']}\nRaça: {key['raca']}\nCor: {key['cor']}\nID: {key['numid']}')
        case __:
            print('Opção invalida.')
            listar_pets()


#UPDATE
def atualizar_pet(entrada, nome, idade, raca, cor, obs, adotado):
    pet_atualiado = carregar_pet()
    for pet in pet_atualiado:
        if entrada == pet['nome'] or entrada == pet['numid']:
            pet['nome'] = nome         
            pet['cor'] = cor            
            pet['raca'] = raca            
            pet['idade'] = idade
            pet['obs'] = obs
            pet['adotado'] = adotado
            nome = input('Digite o nome atualizado: ')
            cor = input('Digite a cor atualizada: ')
            raca = input('Digite a raca atualizada: ')
            idade = input('Digite a idade atualizada: ')
            obs = input('Digite a observação: ')
            adotado = input('Pet adotado?\n(1) Sim (0)Não ')
            break
    with open(pets, 'w') as f:
        json.dump(pet_atualiado, f, indent=4)
    print('PET ATUALIZADO')

#DELETE
def deletar_pet(entrada):
    pet_adotado = carregar_pet()
    for pet in pet_adotado:
        if entrada == pet['nome'] or entrada == pet['numid']:
            pet_adotado.remove(pet)  
            break 
    with open(pets, 'w') as f:
        json.dump(pet_adotado, f, indent=4)
    print('PET REMOVIDO!')
    
#TESTE
while (True):
    escolha = int(input('1 add pet\n2 procurar pet\n3 att pet\n4 deletar pet\n'))
    if escolha == 1:
        nome = input('Digite o nome: ')
        idade = input('Digite o idade: ')
        raca = input('Digite o raca: ')
        cor = input('Digite o cor: ')
        adicionar_pet(nome, idade, raca, cor)
    elif escolha == 2:
        listar_pets()
    elif escolha == 3:
        entrada = input('Digite o nome ou id do pet: ')
        atualizar_pet(entrada)
    elif escolha == 4:
        entrada = input('Digite o nome ou id do pet: ')
        deletar_pet(entrada)
    else:
        break