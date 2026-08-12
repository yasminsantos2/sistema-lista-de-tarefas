from pydantic import BaseModel 
from typing import Optional


class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str

 