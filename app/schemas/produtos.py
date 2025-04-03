from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime
from fornecedor import Fornecedor


class Produto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    fornecedor_id: Optional[int] = Field(default=None, foreign_key="fornecedor.id")
    fornecedor: Optional[Fornecedor] = Relationship(back_populates="produtos")
    vendido: int = Field(default=None, index=True)
    data_compra: datetime = Field(index=True)
    data_venda: datetime = Field(default=datetime(0, 0, 0) ,index=True)
    categoria: str = Field(default=None, index=True)
    
