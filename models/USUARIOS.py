from sqlalchemy import Column, Integer, Boolean, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = 'USUARIOS'

    REQUESTER_ID = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    REQUESTER_RUT = Column(String(15), nullable=False)
    REQUESTER_EMAIL = Column(String(40), nullable=False) 
    REQUESTER_NAME = Column(String(45), nullable=False)
    REQUESTER_ALLOWED = Column(Boolean(), nullable=False)
    REQUESTER_USER_ID = Column(String(30), nullable=True)
    REQUESTER_ACTIVITY_DATE = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    REQUESTER_ENTRY_DATE = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
    
    request = relationship("Request", back_populates="requester")
    approver = relationship("Approver", back_populates="requester")

    def __str__(self):
        return f'REQUESTER_ID: {self.REQUESTER_ID}, REQUESTER_RUT: {self.REQUESTER_RUT}, REQUESTER_EMAIL: {self.REQUESTER_EMAIL}, REQUESTER_NAME: {self.REQUESTER_NAME}, REQUESTER_ALLOWED:{self.REQUESTER_ALLOWED}'
    


