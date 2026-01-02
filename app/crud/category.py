from sqlalchemy.orm import Session 
from models.category import  Categoria
from schemas.category import CategoriaCreate
from sqlalchemy import or_


### Categoria CRUD operations

def crear_categorias(db: Session, categoria:CategoriaCreate):
    db_categoria = Categoria(nombre = categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db:Session):
    return db.query(Categoria).all()
