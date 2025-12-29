from fastapi import FastAPI

app = FastAPI()

@app.get("/productos")
def listar_productos():
    return {"productos": ["Producto 1", "Producto 2", "Producto 3"]}