from pydantic import BaseModel

class PetModel(BaseModel):
    nome: str
    idade: int
    raca: str
    cor: str
    obs: str = ""
    adotado: bool = False

    class Config:
        orm_mode = True