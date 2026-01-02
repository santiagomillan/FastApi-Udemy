from fastapi import  Depends, APIRouter
from schemas.category import   CategoriaCreate, CategoriaResponse
from crud.category import  crear_categorias, obtener_categorias
from sqlalchemy.orm import Session
from deps.deps import get_db

api_router = APIRouter()

## Categoria ##
@api_router.post("/categorias", response_model=CategoriaResponse)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return crear_categorias(db, categoria)

@api_router.get("/categorias", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return obtener_categorias(db) 
