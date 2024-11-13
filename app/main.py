from fastapi import FastAPI
from app.routes.products import router as products_router
from app.routes.pets import router as pets_router
from app.routes.clientes import router as clientes_router
from app.routes.funcionarios import router as funcionarios_router

app = FastAPI()

app.include_router(products_router)
app.include_router(pets_router)
app.include_router(clientes_router)
app.include_router(funcionarios_router)
