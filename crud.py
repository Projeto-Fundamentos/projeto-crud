import json
import os

pets = os.path.join(os.path.dirname(__file__), 'pets.json')

def carregar_pet():
    if not os.path.exists(pets):
        with open(pets, 'w') as f:
            json.dump([], f, indent=4)
    with open(pets, 'r') as f:
        return json.load(f)
    
#CREATE    
def adicionar_pet(tipo, raca, nome, idade):
    pet = {
        "tipo": tipo,
        "raca": raca,
        "nome": nome,
        "idade": idade
    }
    novo_pet = carregar_pet()
    novo_pet.append(pet)
    with open(pets, 'w') as f:
        json.dump(novo_pet, f, indent=4)

#READ
def listar_pets():
    pets = carregar_pet()

    print('LISTA DE ANIMAIS PARA ADOÇÃO:')
    for pet in pets:
        print('--------------------------------------------------------------')
        print(f'Tipo: {pet['tipo']}\tRaça: {pet['raca']}\tNome: {pet['nome']}\tIdade: {pet['idade']}')
    print('--------------------------------------------------------------')

#UPDATE
def atualizar_pet(tipo, raca, nome_novo, nome_antigo, idade):
    pet_atualiado = carregar_pet()
    for pet in pet_atualiado:
        if nome_antigo == pet['nome']:
            pet['nome'] = nome_novo            
            pet['tipo'] = tipo            
            pet['raca'] = raca            
            pet['idade'] = idade 
            break
    with open(pets, 'w') as f:
        json.dump(pet_atualiado, f, indent=4)
    print('PET ATUALIZADO')

#DELETE
def adotar_pet(nome):
    pet_adotado = carregar_pet()
    for pet in pet_adotado:
        if nome == pet['nome']:
            print(nome, pet['nome'])
            pet_adotado.remove(pet)
            break
    with open(pets, 'w') as f:
        json.dump(pet_adotado, f, indent=4)
    print('PET ADOTADO!')
    
#TESTE
adicionar_pet('Gato', 'Laranja','Fira', '3')
adicionar_pet('Cachorro', 'Pitbull','Vagas', '5')
adicionar_pet('Gato', 'Magro', 'Pelua', '3')
adicionar_pet('Cachorro', 'Salsicha','Scooby', '10')

atualizar_pet('Arara', 'Azul', 'Blue', 'Fira', 2)

adotar_pet('Pelua')

listar_pets()