from pydantic import BaseModel

class Servico(BaseModel):
    servico_id: str = None
    nome: str
    descricao: str
    duracao: int

    class Config:
        orm_mode = True
