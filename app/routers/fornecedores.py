from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Annotated
from sqlmodel import Session, select
from ..schemas.fornecedor import Fornecedor 
from ..database.session import get_session
from app.schemas import fornecedor


router = APIRouter(prefix='/fornecedores', tags=['fornecedores'])


SessionDep = Annotated[Session, Depends(get_session)]

# crud dos fornecedores

# adicionar um fornecedor
@router.post('/')
def adicionar_fornecedor(fornecedor: Fornecedor, session: SessionDep):
    session.add(fornecedor)
    session.commit()
    session.refresh(fornecedor)
    return fornecedor
    
# toma no cu broca do carai

# pegar os produtos de um fornecedor especifico
@router.get('/{fornecedor_id}')
def produtos_fornecedor(fornecedor_id: int, session: SessionDep):
    query = select(Fornecedor).where(Fornecedor.id == fornecedor_id)
    fornecedor_escolhido = session.exec(query).first()
    if not fornecedor_escolhido:
        raise HTTPException(404, "O fornecedor nao foi encontrado")
    return [fornecedor_escolhido.produtos, fornecedor_escolhido.nome]


