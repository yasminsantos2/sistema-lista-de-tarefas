from fastapi import APIRouter
from app.modelos.tarefas import Tarefa  

router = APIRouter(
    prefix="/tarefas",
)

LISTAR_TAREFAS = [
        {"id": 1, "titulo": "Tarefa 1", "descricao": "Descrição da Tarefa 1"},
        {"id": 2, "titulo": "Tarefa 2", "descricao": "Descrição da Tarefa 2"},
        {"id": 3, "titulo": "Tarefa 3", "descricao": "Descrição da Tarefa 3"},
    ]


@router.get("/")
async def listar_tarefas():

    return LISTAR_TAREFAS


@router.get("/{tarefa_id}", response_model=Tarefa | None)
async def obter_tarefa(tarefa_id: int):
    for tarefa in LISTAR_TAREFAS:
        if tarefa["id"] == tarefa_id:
            return tarefa
    return None


