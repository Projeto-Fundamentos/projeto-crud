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
def adicionar_pet(obs = "", adotado = 0):
    nome = input('Digite o nome: ')
    while True:
        try:
            idade = int(input("Digite a idade: "))
            break
        except ValueError:
            print("Erro: Por favor, digite um número inteiro.")
    raca = input('Digite o raca: ')
    cor = input('Digite o cor: ')
    pet = {
        "numid": gerar_id(),
        "nome": nome,
        "idade": idade,
        "raca": raca,
        "cor": cor,
        "obs": obs,
        "adotado": adotado
    }
    lista_pets = carregar_pet()
    lista_pets.append(pet)
    with open(pets, 'w') as f:
        json.dump(lista_pets, f, indent=4)
    print('Pet adicionado!')

#READ
def listar_pets():
    lista_pets = carregar_pet()
    opcao = int(input('(1) Listar pet por idade.\n(2) Listar pet por raça.\n(3) Achar pet pelo nome.\n'))
    match opcao:
        case 1:
            pets_por_idade = sorted(lista_pets, key=lambda pet: pet['idade'])
            for key in pets_por_idade:
                print('-'*150)
                print(f'Nome: {key['nome']}\tIdade: {key['idade']}\tRaça: {key['raca']}\tCor: {key['cor']}\tID: {key['numid']}')
            print('-'*150)
            return pets_por_idade
        case 2:
            pets_por_raca = sorted(lista_pets, key=lambda pet: pet['raca'])
            for key in pets_por_raca:
                print('-'*150)
                print(f'Nome: {key['nome']}\tIdade: {key['idade']}\tRaça: {key['raca']}\tCor: {key['cor']}\tID: {key['numid']}')
            print('-'*150)
        case 3:
            entrada = input('Digite o nome ou ID do pet: ')
            for key in lista_pets:
                if entrada == key['nome'] or entrada == key['numid']:
                    print(f'Nome: {key['nome']}\nIdade: {key['idade']}\nRaça: {key['raca']}\nCor: {key['cor']}\nID: {key['numid']}')
        case __:
            print('Opção invalida.')
            listar_pets()


#UPDATE
def atualizar_pet():
    lista_pets = carregar_pet()
    entrada = input('Digite o nome ou ID do pet: ')
    for key in lista_pets:
        if entrada == key['nome'] or entrada == key['numid']:
            nome = input('Digite o nome atualizado: ')
            cor = input('Digite a cor atualizada: ')
            raca = input('Digite a raca atualizada: ')
            while True:
                try:
                    idade = int(input("Digite a idade: "))
                    break
                except ValueError:
                    print("Erro: Por favor, digite um número inteiro.")
            obs = input('Digite a observação: ')
            adotado = input('Pet adotado?\n(1) Sim (0)Não ')
            key['nome'] = nome         
            key['cor'] = cor            
            key['raca'] = raca            
            key['idade'] = idade
            key['obs'] = obs
            key['adotado'] = adotado
            with open(pets, 'w') as f:
                json.dump(lista_pets, f, indent=4)
            print('Informações atualizadas!')
            break
        else:
            print('Pet não encontrado.')


#DELETE
def deletar_pet():
    lista_pets = carregar_pet()
    entrada = input('Digite o nome ou id do pet: ')
    for key in lista_pets:
        if entrada == key['nome'] or entrada == key['numid']:
            lista_pets.remove(key)  
            with open(pets, 'w') as f:
                json.dump(lista_pets, f, indent=4)
            print('Pet removido!')
            break
        else:
            print('Pet não encontrado')
    
#TESTE
while (True):
    escolha = int(input('1 add pet\n2 procurar pet\n3 att pet\n4 deletar pet\n'))
    if escolha == 1:
        adicionar_pet()
    elif escolha == 2:
        listar_pets()
    elif escolha == 3:
        atualizar_pet()
    elif escolha == 4:
        deletar_pet()
    else:
        break