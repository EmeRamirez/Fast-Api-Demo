from config.dbconfig import Base
from sqlalchemy import Column, Integer, Boolean, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class UsuarioModel(Base):
    __tablename__ = 'USUARIOS'

    USER_ID = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    NAME = Column(String(40), nullable=False)
    AGE = Column(Integer(), nullable=False)
    EMAIL = Column(String(40), nullable=False) 
    CREATED_AT = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
    
    department = relationship("DepartmentModel", back_populates="usuario") # Esta misma relación se construiría en la definición de la tabla DEPARTMENTS
    

    def __str__(self):
        return f'USER_ID: {self.USER_ID}, NAME: {self.NAME}, AGE: {self.AGE}, EMAIL: {self.EMAIL}'
    


