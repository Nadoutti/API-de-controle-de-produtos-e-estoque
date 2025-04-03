from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Annotated
from sqlmodel import Session, select
from ..schemas.produtos import Produto
from ..database.session import get_session


router = APIRouter(prefix='/produtos', tags=['produtos'])


SessionDep = Annotated[Session, Depends(get_session)]

# CRUD DOS PRODUTOS

# pegar um produto especifico

@router.get('/{produto_id}')
def get_produto(produto_id: int, session: SessionDep):
    produto = session.get(Produto, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return produto

# produtos que foram vendidos

@router.get('/vendidos')
def get_produtos_vendidos(session: SessionDep, limit: Annotated[int, Query(le=100)] = 100, offset: int = 0):
    produtos = session.exec(select(Produto).offset(offset).limit(limit)).all()
    if not produtos:
        raise HTTPException(status_code=404, detail="Produtos nao encontrados")
    return produtos

# produtos por fornecedor

# adicionar um produto
@router.post('/')
def create_produto(produto: Produto, session: SessionDep):
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto

