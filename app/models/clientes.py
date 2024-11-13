from pydantic import BaseModel

class ClienteModel(BaseModel):
    nome: str
    telefone: str
    endereco: str
    idade: int
    adotado: bool = False

    class Config:
        orm_mode = True
