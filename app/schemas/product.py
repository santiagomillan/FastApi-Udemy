from pydantic import BaseModel



## Producto
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    # stock: int
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int 
    class Config:
        from_attributes = True