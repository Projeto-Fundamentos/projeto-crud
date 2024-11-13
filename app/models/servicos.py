from pydantic import BaseModel

class Servico(BaseModel):
    nome: str
    descricao: str
    duracao: int 