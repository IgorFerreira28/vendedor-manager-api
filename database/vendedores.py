# api/database/vendedores.py

from sqlalchemy import Column, Integer, String, Date
from database.base import Base

# Modelo dos dados do vendedor
class Vendedor(Base):
    __tablename__ = "sellers"

    cpf = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    nascimento = Column(String, index=True, nullable=False)
    uf = Column(String, index=True, nullable=False)