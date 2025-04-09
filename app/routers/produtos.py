import datetime
from fastapi import APIRouter, Depends, HTTPException
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
def get_produtos_vendidos(session: SessionDep):
    query = select(Produto).where(Produto.vendido == 1)
    produtos = session.exec(query).all()
    if not produtos:
        raise HTTPException(status_code=404, detail="Produtos nao encontrados")
    tamanho_lista = len(produtos)
    tamanho_filtro: int = round(tamanho_lista / 2)
    return produtos[: tamanho_filtro]


# adicionar um produto
@router.post('/')
def create_produto(produto: Produto, session: SessionDep):
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto


# listar produtos vendidos em um certo periodo de tempo
@router.get('/vendidos/ultimoMes')
def get_vendidos_ultimo_mes(session: SessionDep):
    ultimos_trinta_dias = datetime.datetime.now() - datetime.timedelta(30)
    query = select(Produto).where(Produto.vendido == 1, Produto.data_venda >= ultimos_trinta_dias.date())
    produtos = session.exec(query).all()
    return produtos 
    
# listar produtos nao vendidos
@router.get('/estoque')
def get_nao_vendidos(session: SessionDep):
    query = select(Produto).where(Produto.vendido == 0)
    produtos = session.exec(query).all()
    
    if not produtos:
        raise HTTPException(404, "Produtos nao encontrados")
    return produtos

# listar nao vendidos por categoria
@router.get('/naoVendidos/{categoria}')
def get_nao_vendidos_categoria(categoria: str, session: SessionDep):
    query = select(Produto).where(Produto.vendido == 0, Produto.categoria == categoria)
    produtos = session.exec(query).all()

    if not produtos:
        raise HTTPException(404, "Produtos nao encontrados")

    return produtos

