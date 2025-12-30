from pydantic import BaseModel




class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    stock: int
    categoria_id: int


class ProductoResponse(ProductoCreate):
    id: int 
    class Config:
        orm_mode = True