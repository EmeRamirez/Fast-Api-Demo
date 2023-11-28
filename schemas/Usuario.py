#Importar pydantic para schema
from pydantic import BaseModel #Esto nos permite crear schemas de datos

class ModeloUsuario(BaseModel):
    NAME: str
    AGE: int
    GENDER: str

class RespuestaUsuario(BaseModel):
    NAME: str
    AGE: int