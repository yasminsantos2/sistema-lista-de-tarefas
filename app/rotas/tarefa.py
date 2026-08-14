from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from app.dependencias import obter_tarefa_repositorio
from app.modelos.tarefa import Tarefa, TarefaCriarAtualizar
from app.banco_de_dados.tarefa_repository import TarefaRepositorio

router = APIRouter(
    prefix="/tarefas",
)


# ROTA PARA LISTAR TODAS AS TAREFAS
@router.get("/", response_model=list[Tarefa])
async def listar_tarefas(
    tarefa_repositorio: Annotated[TarefaRepositorio, Depends(obter_tarefa_repositorio)]
):
    return await tarefa_repositorio.listar_tarefas()


# ROTA PARA OBTER UMA TAREFA PELO ID
@router.get("/{tarefa_id}", response_model=Tarefa)
async def obter_tarefa(
    tarefa_id: int,
    tarefa_repositorio: Annotated[TarefaRepositorio, Depends(obter_tarefa_repositorio)]
):
    tarefa = await tarefa_repositorio.obter_tarefa(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


# ROTA PARA CRIAR UMA NOVA TAREFA
@router.post("/", response_model=Tarefa, status_code=201)
async def criar_tarefa(
    tarefa: TarefaCriarAtualizar,
    tarefa_repositorio: Annotated[TarefaRepositorio, Depends(obter_tarefa_repositorio)]
):
    return await tarefa_repositorio.criar_tarefa(tarefa)


# ROTA PARA ATUALIZAR UMA TAREFA EXISTENTE
@router.put("/{tarefa_id}", response_model=Tarefa)
async def atualizar_tarefa(
    tarefa_id: int,
    tarefa: TarefaCriarAtualizar,
    tarefa_repositorio: Annotated[TarefaRepositorio, Depends(obter_tarefa_repositorio)]
):
    tarefa_atualizada = await tarefa_repositorio.atualizar_tarefa(tarefa_id, tarefa)
    if tarefa_atualizada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada


# ROTA PARA DELETAR UMA TAREFA
@router.delete("/{tarefa_id}")
async def deletar_tarefa(
    tarefa_id: int,
    tarefa_repositorio: Annotated[TarefaRepositorio, Depends(obter_tarefa_repositorio)]
):
    sucesso = await tarefa_repositorio.deletar_tarefa(tarefa_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"status": "sucesso", "mensagem": "Tarefa deletada com sucesso"}
