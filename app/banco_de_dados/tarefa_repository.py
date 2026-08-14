from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelos.tarefa import Tarefa
from app.modelos.tarefa import TarefaCriarAtualizar


# Faz a ponte entre o banco (linhas SQL) e os objetos Tarefa.
class TarefaRepositorio:

    # Recebe o banco de fora (injeção de dependência).
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
        self.bd = banco_de_dados

    # Retorna todas as tarefas como lista de objetos Tarefa.
    async def listar_tarefas(self) -> list[Tarefa]:
        with self.bd.conectar() as conexao:           # abre e fecha conexão sozinho
            cursor = conexao.cursor()                 # ponteiro para executar SQL
            cursor.execute("SELECT id, titulo, descricao FROM tarefa")
            linhas = cursor.fetchall()                # traz todas as linhas (tuplas)

            # Converte cada tupla em um objeto Tarefa.
            lista_tarefas = [
                Tarefa(
                    id=linha[0],
                    titulo=linha[1],
                    descricao=linha[2]
                )
                for linha in linhas
            ]
            return lista_tarefas

    async def obter_tarefa(self, tarefa_id: int) -> Tarefa | None:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id, titulo, descricao FROM tarefa WHERE id = ?",
                (tarefa_id,)
            )
            linha = cursor.fetchone()  # traz apenas uma linha (tupla)

            if linha is None:
                return None

            return Tarefa(
                id=linha[0],
                titulo=linha[1],
                descricao=linha[2]
            )

    async def criar_tarefa(self, tarefa: TarefaCriarAtualizar) -> Tarefa:

        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO tarefa (titulo, descricao) VALUES (?, ?)",
                (tarefa.titulo, tarefa.descricao),
            )
            tarefa_id = cursor.lastrowid
        return Tarefa(id=tarefa_id, titulo=tarefa.titulo, descricao=tarefa.descricao)


    
    async def atualizar_tarefa(self, tarefa_id: int, tarefa: TarefaCriarAtualizar) -> Tarefa | None:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE tarefa SET titulo = ?, descricao = ? WHERE id = ?",
                (tarefa.titulo, tarefa.descricao, tarefa_id)
            )
            rowcount = cursor.rowcount
        if rowcount == 0:
            return None
        return Tarefa(id=tarefa_id, titulo=tarefa.titulo, descricao=tarefa.descricao)




    async def deletar_tarefa(self, tarefa_id: int) -> bool:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM tarefa WHERE id = ?", (tarefa_id,)
            )
            return cursor.rowcount > 0