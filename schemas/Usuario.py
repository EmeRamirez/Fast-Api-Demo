#Importar pydantic para schema
from pydantic import BaseModel #Esto nos permite crear schemas de datos

class ModeloUsuario(BaseModel):
    USER_ID: int
    NAME: str
    AGE: int
    EMAIL: str

class RespuestaUsuario(BaseModel):
    NAME: str
    AGE: int