from fastapi import APIRouter, HTTPException
from crud.servicos import adicionar_servicos, listar_por_nome, listar_por_descricao, listar_por_duracao, achar_por_id, atualizar_servicos, remover_servicos
from models.funcionarios import Servico

router = APIRouter()

@router.post("/servicos/", response_model=Servico)
def criar_servico(servico: Servico):
    try:
        adicionar_servicos(servico.nome, servico.descricao, servico.duracao)
        return servico
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar serviço: {e}")

@router.get("/servicos/nome", response_model=list)
def listar_servicos_nome():
    try:
        servicos = listar_por_nome()
        return [Servico(servico_id=id, **dados) for id, dados in servicos.items()]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar serviços por nome: {e}")

@router.get("/servicos/descricao", response_model=list)
def listar_servicos_descricao():
    try:
        servicos = listar_por_descricao()
        return [Servico(servico_id=id, **dados) for id, dados in servicos.items()]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar serviços por descrição: {e}")

@router.get("/servicos/duracao", response_model=list)
def listar_servicos_duracao():
    try:
        servicos = listar_por_duracao()
        return [Servico(servico_id=id, **dados) for id, dados in servicos.items()]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar serviços por duração: {e}")

@router.get("/servicos/{id}", response_model=Servico)
def buscar_servico(id: str):
    servico = achar_por_id(id)
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return Servico(servico_id=id, **servico)

@router.put("/servicos/{id}", response_model=Servico)
def atualizar_servico(id: str, servico: Servico):
    if not atualizar_servicos(id, servico.nome, servico.descricao, servico.duracao):
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return servico

@router.delete("/servicos/{id}")
def deletar_servico(id: str):
    if not remover_servicos(id):
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return {"message": "Serviço removido com sucesso"}
