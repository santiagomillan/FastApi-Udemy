from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from crud.product import actualizar_producto,crear_producto, eliminar_producto, obtener_producto, obtener_productos,Producto, ProductoCreate, ProductoResponse, Session
from deps.deps import get_db, require_admin



from fastapi import APIRouter


api_router = APIRouter()

@api_router.get("/productos", response_model=list[ProductoCreate])
def listar_productos(db: Session = Depends(get_db)):
    return obtener_productos(db)
    

@api_router.post("/productos", response_model=ProductoCreate, dependencies=[Depends(require_admin)])
def agregar_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto(db, producto)

@api_router.put("/productos/{id}" , response_model=ProductoCreate)
def actualizar_producto(producto_id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
    producto = actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@api_router.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"detail": "Producto eliminado exitosamente"}
