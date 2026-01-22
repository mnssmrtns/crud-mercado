import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from database import Database
from main_ui import MainWindow, LoginWindow

class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.db = Database()
        
        # Iniciar com a tela de Login
        self.login_window = LoginWindow()
        self.login_window.btn_login.clicked.connect(self.check_login)
        self.login_window.show()
        
        self.main_window = None

    def check_login(self):
        email = self.login_window.input_email.text()
        senha = self.login_window.input_senha.text()
        
        if email == "admin" and senha == "1234":
            self.login_window.close()
            self.open_main_window()
        else:
            QMessageBox.warning(self.login_window, "Erro", "Email ou senha incorretos!")

    def open_main_window(self):
        self.main_window = MainWindow()
        
        # Conexões CLIENTES
        self.main_window.btn_add_cli.clicked.connect(self.add_cliente)
        self.main_window.btn_upd_cli.clicked.connect(self.update_cliente)
        self.main_window.btn_del_cli.clicked.connect(self.delete_cliente)
        self.main_window.table_cli.cellClicked.connect(self.fill_fields_cliente)
        
        # Conexões PRODUTOS
        self.main_window.btn_add_prod.clicked.connect(self.add_produto)
        self.main_window.btn_upd_prod.clicked.connect(self.update_produto)
        self.main_window.btn_del_prod.clicked.connect(self.delete_produto)
        self.main_window.table_prod.cellClicked.connect(self.fill_fields_produto)

        self.load_clientes()
        self.load_produtos()
        self.main_window.show()

    # --- LÓGICA CLIENTES ---
    def load_clientes(self):
        self.main_window.table_cli.setRowCount(0)
        users = self.db.get_clientes()
        for row, data in enumerate(users):
            self.main_window.table_cli.insertRow(row)
            for col, val in enumerate(data):
                self.main_window.table_cli.setItem(row, col, QTableWidgetItem(str(val)))

    def add_cliente(self):
        nome = self.main_window.cli_nome.text()
        email = self.main_window.cli_email.text()
        senha = self.main_window.cli_senha.text()
        if nome and email and senha:
            self.db.add_cliente(nome, email, senha)
            self.clear_fields_cliente()
            self.load_clientes()
        else:
            QMessageBox.warning(self.main_window, "Aviso", "Preencha todos os campos!")

    def update_cliente(self):
        row = self.main_window.table_cli.currentRow()
        if row >= 0:
            uid = self.main_window.table_cli.item(row, 0).text()
            nome = self.main_window.cli_nome.text()
            email = self.main_window.cli_email.text()
            senha = self.main_window.cli_senha.text()
            self.db.update_cliente(uid, nome, email, senha)
            self.load_clientes()
            self.clear_fields_cliente()

    def delete_cliente(self):
        row = self.main_window.table_cli.currentRow()
        if row >= 0:
            uid = self.main_window.table_cli.item(row, 0).text()
            self.db.delete_cliente(uid)
            self.load_clientes()
            self.clear_fields_cliente()

    def fill_fields_cliente(self):
        row = self.main_window.table_cli.currentRow()
        self.main_window.cli_nome.setText(self.main_window.table_cli.item(row, 1).text())
        self.main_window.cli_email.setText(self.main_window.table_cli.item(row, 2).text())
        self.main_window.cli_senha.setText(self.main_window.table_cli.item(row, 3).text())
    
    def clear_fields_cliente(self):
        self.main_window.cli_nome.clear()
        self.main_window.cli_email.clear()
        self.main_window.cli_senha.clear()

    # --- LÓGICA PRODUTOS ---
    def load_produtos(self):
        self.main_window.table_prod.setRowCount(0)
        produtos = self.db.get_produtos()
        for row, data in enumerate(produtos):
            self.main_window.table_prod.insertRow(row)
            for col, val in enumerate(data):
                self.main_window.table_prod.setItem(row, col, QTableWidgetItem(str(val)))

    def add_produto(self):
        nome = self.main_window.prod_nome.text()
        preco = self.main_window.prod_preco.text()
        qtd = self.main_window.prod_qtd.text()
        if nome and preco and qtd:
            try:
                self.db.add_produto(nome, float(preco), int(qtd))
                self.clear_fields_produto()
                self.load_produtos()
            except ValueError:
                QMessageBox.warning(self.main_window, "Erro", "Preço deve ser número e Qtd inteiro.")
        else:
            QMessageBox.warning(self.main_window, "Aviso", "Preencha todos os campos!")

    def update_produto(self):
        row = self.main_window.table_prod.currentRow()
        if row >= 0:
            uid = self.main_window.table_prod.item(row, 0).text()
            nome = self.main_window.prod_nome.text()
            preco = self.main_window.prod_preco.text()
            qtd = self.main_window.prod_qtd.text()
            self.db.update_produto(uid, nome, preco, qtd)
            self.load_produtos()
            self.clear_fields_produto()

    def delete_produto(self):
        row = self.main_window.table_prod.currentRow()
        if row >= 0:
            uid = self.main_window.table_prod.item(row, 0).text()
            self.db.delete_produto(uid)
            self.load_produtos()
            self.clear_fields_produto()

    def fill_fields_produto(self):
        row = self.main_window.table_prod.currentRow()
        self.main_window.prod_nome.setText(self.main_window.table_prod.item(row, 1).text())
        self.main_window.prod_preco.setText(self.main_window.table_prod.item(row, 2).text())
        self.main_window.prod_qtd.setText(self.main_window.table_prod.item(row, 3).text())

    def clear_fields_produto(self):
        self.main_window.prod_nome.clear()
        self.main_window.prod_preco.clear()
        self.main_window.prod_qtd.clear()

if __name__ == "__main__":
    controller = AppController()
    sys.exit(controller.app.exec())