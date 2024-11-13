from fastapi import APIRouter
from typing import List
from app.crud.funcionarios import add_funcionario, listar_funcionarios, excluir_funcionario, atualizar_funcionario
from app.models.funcionarios import Funcionario

router = APIRouter()

@router.get("/funcionarios", response_model=List[Funcionario])
def get_funcionarios():
    funcionarios = listar_funcionarios()
    return [Funcionario(**dados) for dados in funcionarios.values()]  # Converte o dicionário em modelos Funcionario

@router.post("/funcionarios")
def add_new_funcionario(funcionario: Funcionario):
    add_funcionario(funcionario)
    return {"message": "Funcionário adicionado com sucesso!"}

@router.delete("/funcionarios/{id_funcionario}")
def delete_funcionario(id_funcionario: str):
    if excluir_funcionario(id_funcionario):
        return {"message": f"Funcionário {id_funcionario} excluído com sucesso!"}
    return {"error": "Funcionário não encontrado."}

@router.put("/funcionarios/{id_funcionario}")
def update_funcionario(id_funcionario: str, funcionario: Funcionario):
    if atualizar_funcionario(id_funcionario, funcionario):
        return {"message": f"Funcionário {id_funcionario} atualizado com sucesso!"}
    return {"error": "Funcionário não encontrado."}
