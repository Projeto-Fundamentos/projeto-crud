from fastapi import APIRouter, HTTPException
from app.models.clientes import ClienteModel
from app.crud.clientes import adicionar_cliente, listar_clientes, atualizar_cliente, deletar_cliente

router = APIRouter()

@router.post("/clientes/")
def create_cliente(cliente_data: ClienteModel):
    id_cliente = adicionar_cliente(cliente_data)
    return {"id_cliente": id_cliente}

@router.get("/clientes/")
def get_clientes():
    clientes = listar_clientes()
    if not clientes:
        raise HTTPException(status_code=404, detail="Nenhum cliente encontrado.")
    return clientes

@router.put("/clientes/{id_cliente}")
def update_cliente(id_cliente: str, cliente_data: ClienteModel):
    sucesso = atualizar_cliente(id_cliente, cliente_data)
    if sucesso:
        return {"message": "Cliente atualizado com sucesso!"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")

@router.delete("/clientes/{id_cliente}")
def delete_cliente(id_cliente: str):
    sucesso = deletar_cliente(id_cliente)
    if sucesso:
        return {"message": f"Cliente {id_cliente} excluído com sucesso!"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")
