from fastapi import FastAPI

app = FastAPI()


"""
**PARA INICIAR EL SERVIDOR**
fastapi dev (api.py) --> NOMBRE DE TU ARCHIVO

**PARA VER DOCUMENTACIÓN DE LA API**
/docs para ver la documentación de la API en Swagger    
/redoc para ver la documentación de la API en ReDoc
"""


@app.get("/")
async def root():
    return "¡Hola FastApi!"


@app.get("/url")
async def url():
    return {"url":"https://mouredev.com/python"}


