# Se importa la instancia de FastAPI
from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
app = FastAPI() #Se inicializa



#Incluyendo rutas
from routes.usuarios import usuarios

app.include_router(usuarios)

#Crear la primera ruta de prueba en root
@app.get('/ping')
def ping():
    return 'pong'

@app.get('/duplicar/{num}', status_code=status.HTTP_200_OK)
def wea(num: int):
    try:
        new_num = num * 2
        return new_num
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

from sqlalchemy import text
from config.dbconfig import SessionLocal

@app.get("/check_db_connection")
def check_db_connection():
    try:
        session = SessionLocal()
        # Intenta realizar una consulta simple para verificar la conexión
        session.execute(text("SELECT 1"))
        return {"message": "Database connection is alive"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection error: {str(e)}"
        )

#Para ejecutar el proyecto utilizamos uvicorn -> uvicorn main:app 
# Se puede agregar reload --reload
#Se puede establecer un puerto especifico --port 7080