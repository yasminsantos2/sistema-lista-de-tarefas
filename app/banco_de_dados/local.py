# ============================================================
# BLOCO 1 - IMPORTAÇÕES
# ============================================================
# sqlite3:
# Biblioteca nativa do Python que permite criar e manipular
# bancos de dados SQLite.
#
# contextmanager:
# Permite criar um gerenciador de contexto, para usar o método
# conectar() com o comando "with", garantindo que a conexão
# seja aberta e fechada corretamente.
# ============================================================

import sqlite3
from contextlib import contextmanager


# ============================================================
# BLOCO 2 - CLASSE RESPONSÁVEL PELO BANCO DE DADOS
# ============================================================
# Esta classe é responsável por gerenciar toda a conexão com o
# banco SQLite.
#
# Suas responsabilidades são:
# • Abrir a conexão.
# • Fechar a conexão.
# • Fazer commit das alterações.
# • Fazer rollback em caso de erro.
# • Criar a tabela caso ela ainda não exista.
# ============================================================

class BancoDeDadosLocal():

    # ========================================================
    # BLOCO 3 - CONSTRUTOR
    # ========================================================
    # Executado automaticamente quando fazemos:
    #
    # db = BancoDeDadosLocal()
    #
    # O construtor:
    # 1. Guarda o nome do arquivo do banco.
    # 2. Chama o método que cria a tabela, se necessário.
    # ========================================================

    def __init__(self, nome_arquivo='tarefa.db'):
        self.nome_arquivo = nome_arquivo
        self.inicializar_banco()

    # ========================================================
    # BLOCO 4 - GERENCIADOR DE CONEXÃO
    # ========================================================
    # Este método controla todo o ciclo de vida da conexão.
    #
    # Fluxo:
    #
    # 1. Abre a conexão.
    # 2. Entrega a conexão para quem chamou.
    # 3. Se tudo der certo → commit().
    # 4. Se ocorrer erro → rollback().
    # 5. Sempre fecha a conexão.
    #
    # Graças ao @contextmanager podemos utilizá-lo assim:
    #
    # with self.conectar() as conexao:
    # ========================================================

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

    # ========================================================
    # BLOCO 5 - CRIAÇÃO DA TABELA
    # ========================================================
    # Este método é chamado pelo construtor.
    #
    # Sua função é garantir que a tabela "livro"
    # exista no banco de dados.
    #
    # Caso a tabela já exista,
    # o comando CREATE TABLE IF NOT EXISTS
    # simplesmente não faz nada.
    # ========================================================

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