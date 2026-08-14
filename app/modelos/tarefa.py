from pydantic import BaseModel 

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str

class TarefaCriarAtualizar(BaseModel):
    titulo: str
    descricao: str 

 