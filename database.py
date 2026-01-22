import sqlite3

class Database:
    def __init__(self, db_name="mercado.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
        
    def create_tables(self):
        # Tabela Clientes
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        """)
        # Tabela Produtos
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    # --- CRUD CLIENTES ---
    def add_cliente(self, nome, email, senha):
        self.cursor.execute("INSERT INTO clientes (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        self.connection.commit()

    def get_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def update_cliente(self, id, nome, email, senha):
        self.cursor.execute("UPDATE clientes SET nome = ?, email = ?, senha = ? WHERE id = ?", (nome, email, senha, id))
        self.connection.commit()

    def delete_cliente(self, id):
        self.cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
        self.connection.commit()

    # --- CRUD PRODUTOS ---
    def add_produto(self, nome, preco, quantidade):
        self.cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
        self.connection.commit()

    def get_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def update_produto(self, id, nome, preco, quantidade):
        self.cursor.execute("UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?", (nome, preco, quantidade, id))
        self.connection.commit()

    def delete_produto(self, id):
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        self.connection.commit()