import os
import json
from config import DATA_PATHS
from app.models.pets import PetModel

pets_file = DATA_PATHS['pets']

def carregar_pets():
    if not os.path.exists(pets_file):
        with open(pets_file, 'w') as f:
            json.dump({}, f, indent=4)
    with open(pets_file, 'r') as f:
        return json.load(f)

def gerar_id():
    data = carregar_pets()
    if data:
        maxId = max(int(petId) for petId in data.keys())
        return str(maxId + 1)
    return "1"

def adicionar_pet(pet_data: PetModel):
    lista_pets = carregar_pets()
    novo_pet_id = gerar_id()
    lista_pets[novo_pet_id] = pet_data.dict() 

    with open(pets_file, 'w') as f:
        json.dump(lista_pets, f, indent=4)
    return novo_pet_id

def listar_por_idade():
    lista_pets = carregar_pets()
    return dict(sorted(lista_pets.items(), key=lambda pet: int(pet[1]['idade'])))

def listar_por_raca():
    lista_pets = carregar_pets()
    return dict(sorted(lista_pets.items(), key=lambda pet: pet[1]['raca']))

def achar_por_id(id):
    lista_pets = carregar_pets()
    return lista_pets.get(id, "Pet não encontrado")

def atualizar_pet(id: str, pet_data: PetModel):
    lista_pets = carregar_pets()
    pet = lista_pets.get(id)

    if pet:
        lista_pets[id] = pet_data.dict() 

        with open(pets_file, 'w') as f:
            json.dump(lista_pets, f, indent=4)
        return f"Pet {id} atualizado com sucesso"
    return "Pet não encontrado"

def remover_pet(id: str):
    lista_pets = carregar_pets()
    if id in lista_pets:
        del lista_pets[id]
        with open(pets_file, 'w') as f:
            json.dump(lista_pets, f, indent=4)
        return f"Pet {id} removido com sucesso"
    return "Pet não encontrado"
