from fastapi import status, HTTPException, APIRouter

#Importamos un schema
from schemas.Usuario import ModeloUsuario, RespuestaUsuario

usuarios = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@usuarios.get('/')
def get_usuarios():
    try:
        return "esta es la lista de usuarios"
    except Exception as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
    

@usuarios.post('/nuevo', response_model=RespuestaUsuario, status_code=status.HTTP_201_CREATED)
def insert_user(user: ModeloUsuario):
    try:
        print(user)
        return user
    except Exception as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))