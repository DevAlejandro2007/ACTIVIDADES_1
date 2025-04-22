from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
**PARA INICIAR EL SERVIDOR**
fastapi dev (api.py) --> NOMBRE DE TU ARCHIVO

**PARA VER DOCUMENTACIÓN DE LA API**
/docs para ver la documentación de la API en Swagger    
/redoc para ver la documentación de la API en ReDoc
"""

# Entidad User
class User(BaseModel):
    id : int 
    name: str
    surname: str
    url: str
    age : int

class Admin(BaseModel):
    id: int
    name: str
    surname: str 
    rol: str
    age: int 

#Lista de Usuarios 
users_list = [User(id = 1 ,name = "Alejo",surname = "Rojas",url = "www.youtube.com",age = 15),
            User(id = 2,name = "Alejandro",surname ="Benitez",url ="www.google.com",age =  15),
            User(id = 3,name ="x",surname = "z", url= "www.instagram.com",age= 15)]

#Direccion de la lista de usuarios
@app.get("/user")
async def users():
    return users_list

# VIA PATH (URL)
@app.get("/user/{id}")
async def user(id: int):
    return buscar_usuario(id)

# VIA QUERY (URL CON SIGNO DE INTERROGACION )
@app.get("/userquery")
async def user(id: int):
     return buscar_usuario(id)

@app.post("/user")
async def user(user: User):
    if type(buscar_usuario(user.id)) == User:
        return {"ERROR":" EL USUARIO YA EXISTE "}
    else:
        users_list.append(user)
        return user

@app.put("/user")
async def user(user: User):
    
    found = False

    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user
    if not found:
        return {"ERROR":" NO SE HA ENCONTRADO EL USUARIO"}

    

@app.delete("/user/{id}")
async def user(id: int):
    for index, id_user in users_list:
        if users_list[index][id] == id_user:
            users_list.remove[index]
            return {" COMPLETED": " USUARIO ELIMINADO"}

#funcion buscar usuario
def buscar_usuario(id:int):
    users = filter(lambda user: user.id == id, users_list) 
    try:
        return list(users)[0]
    except:
        return {"ERROR": "NO SE HA ENCONTRADO EL USUARIO"}



