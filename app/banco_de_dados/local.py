
import sqlite3
from contextlib import contextmanager

class BancoDeDadosLocal():

    def __init__(self, nome_arquivo='tarefa.db'):
        self.nome_arquivo = nome_arquivo
        self.inicializar_banco()

    @contextmanager
    def conectar(self):

        # Abre uma conexão com o arquivo do banco.
        conexao = sqlite3.connect(self.nome_arquivo)

        try:

            # Entrega a conexão para ser utilizada.
            # A execução pausa aqui até o bloco "with" terminar.
            yield conexao

            # Se nenhuma exceção ocorreu,
            # grava definitivamente as alterações.
            conexao.commit()

        except Exception as e:

            # Se ocorrer algum erro,
            # desfaz todas as alterações realizadas.
            conexao.rollback()

            # Repassa a exceção para quem chamou.
            raise e

        finally:

            # Independente de sucesso ou erro,
            # fecha a conexão com o banco.
            conexao.close()

    def inicializar_banco(self):

        # Abre a conexão utilizando o gerenciador de contexto.
        with self.conectar() as conexao:

            # O cursor é o objeto responsável
            # por executar comandos SQL.
            cursor = conexao.cursor()

            # Executa um comando SQL para criar a tabela.
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tarefa (

                    -- Identificador único da tarefa.
                    -- É gerado automaticamente pelo SQLite.
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    -- Título obrigatório.
                    titulo TEXT NOT NULL,

                    -- Descrição obrigatória.
                    descricao TEXT NOT NULL

                )
            ''')
