# para activar venv

# python -m venv venv

- cd .\venv\Scripts
- .\activate

# instalar dependencias

- pip install fastapi uvicorn

from sqlalchemy import create_engine --> establece coneccion con bd
from sqlalchemy.ext.declarative import declarative_base --> crea las clases de los modelos(tablas en bd)
from sqlalchemy.orm import sessionmaker --> crea sesiones para coneccion con bd

# --

Para crear las tablas ejecutar crear_tablas.py

instalar
pip install 'pydantic[email]' --> valida str (correo)
pip install passlib[bcrypy] --> encripar
