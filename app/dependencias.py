from typing import Annotated
from fastapi import Depends

from app.banco_de_dados.local import BancoDeDadosLocal
from app.banco_de_dados.tarefa_repository import TarefaRepositorio

banco_de_dados = BancoDeDadosLocal()


def obter_banco_de_dados() -> BancoDeDadosLocal:
    return banco_de_dados


def obter_tarefa_repositorio(
    banco_de_dados: Annotated[BancoDeDadosLocal, Depends(obter_banco_de_dados)]
) -> "TarefaRepositorio":
    return TarefaRepositorio(banco_de_dados) 