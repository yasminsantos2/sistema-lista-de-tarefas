from fastapi import APIRouter, Depends,HTTPException
from typing import Annotated

from app.dependencias import obter_tarefa_repositorio
from app.modelos.tarefa import Tarefa  
from app.banco_de_dados.tarefa_repository import TarefaRepositorio



router = APIRouter(
    prefix="/tarefas",
)

LISTAR_TAREFAS = [
        Tarefa(id=1, titulo="Tarefa 1", descricao="Descrição da Tarefa 1"),
        Tarefa(id=2, titulo="Tarefa 2", descricao="Descrição da Tarefa 2"),
        Tarefa(id=3, titulo="Tarefa 3", descricao="Descrição da Tarefa 3"),
    ]


# ROTA PARA LISTAR TODOS OS TAREFA
@router.get("/", response_model=list[Tarefa])
async def listar_tarefas(tarefa_repositorio: Annotated["TarefaRepositorio", Depends(obter_tarefa_repositorio)]):
    return await tarefa_repositorio.listar_tarefas()


# ROTA PARA OBTER UM TAREFA PELO ID
@router.get("/{tarefa_id}", response_model=Tarefa | None)
async def obter_tarefa(tarefa_id: int, tarefa_repositorio: Annotated["TarefaRepositorio", Depends(obter_tarefa_repositorio)]):
        raise HTTPException(status_code=404, detail="Livro não encontrado")


