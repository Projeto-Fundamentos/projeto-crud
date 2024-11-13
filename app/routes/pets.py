from fastapi import APIRouter
from app.crud.pets import adicionar_pet, listar_por_idade, listar_por_raca, achar_por_id, atualizar_pet, remover_pet
from app.models.pets import PetModel

router = APIRouter()

@router.post("/pets/")
def create_pet(pet_data: PetModel):
    pet_id = adicionar_pet(pet_data)
    return {"pet_id": pet_id}

@router.get("/pets/idade/")
def get_pets_by_age():
    pets = listar_por_idade()
    return pets

@router.get("/pets/raca/")
def get_pets_by_breed():
    pets = listar_por_raca()
    return pets

@router.get("/pets/{pet_id}")
def get_pet_by_id(pet_id: str):
    pet = achar_por_id(pet_id)
    return pet

@router.put("/pets/{pet_id}")
def update_pet(pet_id: str, pet_data: PetModel):
    message = atualizar_pet(pet_id, pet_data)
    return {"message": message}

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: str):
    message = remover_pet(pet_id)
    return {"message": message}
