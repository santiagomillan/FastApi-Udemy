from fastapi import FastAPI, Depends, HTTPException, status
# from pydantic import BaseModel
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from deps import require_admin

app = FastAPI()

# class Producto(BaseModel):
#     nombre: str
#     precio: float
#     en_stock: bool


@app.get("/productos", response_model=list[schemas.ProductoCreate])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)
    

@app.post("/productos", response_model=schemas.ProductoCreate, dependencies=[Depends(require_admin)])
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.put("/productos/{id}" , response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"detail": "Producto eliminado exitosamente"}

## Categoria ##
@app.post("/categorias", response_model=schemas.CategoriaResponse)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@app.get("/categorias", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db) 
