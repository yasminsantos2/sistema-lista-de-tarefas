from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from typing import Annotated
from app.rotas.tarefa import router as tarefas_router
from app.banco_de_dados.tarefa_repository import TarefaRepositorio
from app.dependencias import obter_tarefa_repositorio

app = FastAPI(
    title="Sistema Lista de tarefas",
    description="CRM Lista de tarefas",
    version="1.0.0"
)

app.include_router(tarefas_router)


@app.get("/")
async def health_check(
    repo: Annotated[TarefaRepositorio, Depends(obter_tarefa_repositorio)]
):
    # Expor a lista de tarefas diretamente na raiz
    return await repo.listar_tarefas()


@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content = """
    <html>
        <head>
            <title>Sistema lista de tarefas</title>
        </head>
        <body>
            <h1> Sistema Lista de tarefas</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
    return html_content
