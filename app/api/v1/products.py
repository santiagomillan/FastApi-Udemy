from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from deps import require_admin


from fastapi import APIRouter


api_router = APIRouter()

@api_router.get("/productos", response_model=list[schemas.ProductoCreate])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)
    

@api_router.post("/productos", response_model=schemas.ProductoCreate, dependencies=[Depends(require_admin)])
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@api_router.put("/productos/{id}" , response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@api_router.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"detail": "Producto eliminado exitosamente"}
