from sqlmodel import Field, Relationship, SQLModel, true
from typing import List, Optional
from produtos import Produto

# criando a tabela do fornecedor
class Fornecedor(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    produtos: List['Produto'] = Relationship(back_populates="fornecedor")
    nome: str = Field(default=None, index=True)

