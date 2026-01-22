from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
                               QPushButton, QTableWidget, QLabel, QHeaderView, 
                               QTabWidget, QFormLayout, QMessageBox)
from PySide6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Admin")
        self.setFixedSize(300, 200)
        
        layout = QVBoxLayout(self)
        
        self.input_email = QLineEdit(self)
        self.input_email.setPlaceholderText("Email (admin)")
        
        self.input_senha = QLineEdit(self)
        self.input_senha.setPlaceholderText("Senha (1234)")
        self.input_senha.setEchoMode(QLineEdit.Password)
        
        self.btn_login = QPushButton("Entrar")
        
        layout.addWidget(QLabel("<h2>Sistema Mercado</h2>"))
        layout.addWidget(self.input_email)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.btn_login)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestão de Mercado")
        self.setMinimumSize(600, 500)
        
        # Layout Principal com Abas
        self.layout_main = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.layout_main.addWidget(self.tabs)
        
        # --- ABA CLIENTES ---
        self.tab_clientes = QWidget()
        self.setup_tab_clientes()
        self.tabs.addTab(self.tab_clientes, "Clientes")
        
        # --- ABA PRODUTOS ---
        self.tab_produtos = QWidget()
        self.setup_tab_produtos()
        self.tabs.addTab(self.tab_produtos, "Produtos")

    def setup_tab_clientes(self):
        layout = QVBoxLayout(self.tab_clientes)
        
        # Form
        form_layout = QHBoxLayout()
        self.cli_nome = QLineEdit()
        self.cli_nome.setPlaceholderText("Nome Cliente")
        self.cli_email = QLineEdit()
        self.cli_email.setPlaceholderText("Email")
        self.cli_senha = QLineEdit()
        self.cli_senha.setPlaceholderText("Senha")
        self.cli_senha.setEchoMode(QLineEdit.Password)
        
        form_layout.addWidget(self.cli_nome)
        form_layout.addWidget(self.cli_email)
        form_layout.addWidget(self.cli_senha)
        layout.addLayout(form_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_add_cli = QPushButton("Adicionar")
        self.btn_upd_cli = QPushButton("Atualizar")
        self.btn_del_cli = QPushButton("Deletar")
        btn_layout.addWidget(self.btn_add_cli)
        btn_layout.addWidget(self.btn_upd_cli)
        btn_layout.addWidget(self.btn_del_cli)
        layout.addLayout(btn_layout)
        
        # Table
        self.table_cli = QTableWidget(0, 4)
        self.table_cli.setHorizontalHeaderLabels(["ID", "Nome", "Email", "Senha"])
        self.table_cli.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_cli.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.table_cli)

    def setup_tab_produtos(self):
        layout = QVBoxLayout(self.tab_produtos)
        
        # Form
        form_layout = QHBoxLayout()
        self.prod_nome = QLineEdit()
        self.prod_nome.setPlaceholderText("Nome Produto")
        self.prod_preco = QLineEdit()
        self.prod_preco.setPlaceholderText("Preço (R$)")
        self.prod_qtd = QLineEdit()
        self.prod_qtd.setPlaceholderText("Qtd")
        
        form_layout.addWidget(self.prod_nome)
        form_layout.addWidget(self.prod_preco)
        form_layout.addWidget(self.prod_qtd)
        layout.addLayout(form_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_add_prod = QPushButton("Adicionar")
        self.btn_upd_prod = QPushButton("Atualizar")
        self.btn_del_prod = QPushButton("Deletar")
        btn_layout.addWidget(self.btn_add_prod)
        btn_layout.addWidget(self.btn_upd_prod)
        btn_layout.addWidget(self.btn_del_prod)
        layout.addLayout(btn_layout)
        
        # Table
        self.table_prod = QTableWidget(0, 4)
        self.table_prod.setHorizontalHeaderLabels(["ID", "Produto", "Preço", "Qtd"])
        self.table_prod.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_prod.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.table_prod)