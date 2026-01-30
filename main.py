from fastapi import FastAPI

# Crear la app de FastAPI
app = FastAPI()

# Ruta que retorna un saludo
@app.get("/saludos/hola")
def saludo():
    """
    Devuelve un mensaje de saludo.
    """
    return {"mensaje": "¡Hola desde FastAPI con Swagger!"}
