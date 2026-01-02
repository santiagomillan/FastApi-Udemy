from pydantic import BaseModel, EmailStr

## Usuario
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    es_admin: bool = False

class UsuarioResponse(UsuarioBase):
    id: int
    es_admin: bool
    class Config:
        from_attributes = True    
