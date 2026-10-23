from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from contextlib import asynccontextmanager
from typing import Literal

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import TransacaoDB


Base.metadata.create_all(bind=engine)


def obter_banco():
    banco = SessionLocal()
    try:
        yield banco
    finally:
        banco.close()


class Transacao(BaseModel):
    descricao: str = Field(min_length=1, max_length=100)
    tipo: Literal["receita", "despesa"]
    valor: float = Field(gt=0)
    categoria: str = Field(min_length=1, max_length=50)


app = FastAPI(
    title="Controle Financeiro Pessoal",
    description="API para gerenciar receitas e despesas",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static"
)

@app.get("/")
def inicio():
    return FileResponse("frontend/index.html")


@app.post("/transacoes", status_code=201)
def criar_transacao(
    transacao: Transacao,
    banco: Session = Depends(obter_banco)
):
    nova_transacao = TransacaoDB(**transacao.model_dump())

    banco.add(nova_transacao)
    banco.commit()
    banco.refresh(nova_transacao)

    return {
        "mensagem": "Transação cadastrada com sucesso!",
        "transacao": {
            "id": nova_transacao.id,
            "descricao": nova_transacao.descricao,
            "tipo": nova_transacao.tipo,
            "valor": nova_transacao.valor,
            "categoria": nova_transacao.categoria
        }
    }


@app.get("/transacoes")
def listar_transacoes(banco: Session = Depends(obter_banco)):
    return banco.query(TransacaoDB).order_by(
        TransacaoDB.id
    ).all()


@app.get("/resumo")
def obter_resumo(banco: Session = Depends(obter_banco)):
    transacoes = banco.query(TransacaoDB).all()

    total_receitas = sum(
        t.valor for t in transacoes if t.tipo == "receita"
    )
    total_despesas = sum(
        t.valor for t in transacoes if t.tipo == "despesa"
    )

    return {
        "total_receitas": round(total_receitas, 2),
        "total_despesas": round(total_despesas, 2),
        "saldo": round(total_receitas - total_despesas, 2)
    }
