from pydantic import BaseModel

class Funcionario(BaseModel):
    nome: str
    idade: int
    cargo: str
    obs: str = ""
