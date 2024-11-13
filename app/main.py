from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.products import router as products_router
from app.routes.pets import router as pets_router
from app.routes.clientes import router as clientes_router
from app.routes.funcionarios import router as funcionarios_router
from app.routes.servicos import router as servicos_router
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

app.include_router(products_router)
app.include_router(pets_router)
app.include_router(clientes_router)
app.include_router(funcionarios_router)
app.include_router(servicos_router)


@app.get("/pets/create", response_class=HTMLResponse)
async def create_pet_page(request: Request):
    return templates.TemplateResponse("pets/create_pet.html", {"request": request})

@app.get("/pets/read", response_class=HTMLResponse)
async def read_pet_page(request: Request):
    return templates.TemplateResponse("pets/get_pet.html", {"request": request})

@app.get("/pets/update", response_class=HTMLResponse)
async def update_pet_page(request: Request):
    return templates.TemplateResponse("pets/update_pet.html", {"request": request})

@app.get("/pets/delete", response_class=HTMLResponse)
async def delete_pet_page(request: Request):
    return templates.TemplateResponse("pets/delete_pet.html", {"request": request})