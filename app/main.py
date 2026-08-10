from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.rotas.tarefas import router as tarefas_router, listar_tarefas

app = FastAPI(
    title="Sistema Lista de tarefas",
    description="CRM Lista de tarefas",
    version="1.0.0"
)

app.include_router(tarefas_router)


@app.get("/")
async def health_check():
    # Expor a lista de tarefas diretamente na raiz
    return await listar_tarefas()

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
