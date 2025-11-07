import bcrypt
import sqlite3
from datetime import datetime

class Banco:
    def __init__(self, nome_db="banco.db"):
        self.conexao = sqlite3.connect(nome_db)
        self.cursor = self.conexao.cursor()
        self._criar_tabelas()

    def _criar_tabelas(self):
        """Cria tabelas de contas e transações, se não existirem."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                cpf TEXT PRIMARY KEY,
                titular TEXT,
                agencia TEXT,
                numero_conta TEXT,
                senha_hash BLOB,
                saldo REAL DEFAULT 0.0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT,
                tipo TEXT,
                valor REAL,
                data TEXT
            )
        """)
        self.conexao.commit()

    def criar_conta(self, titular, cpf, agencia, numero_conta, senha):
        """Cria nova conta com senha criptografada."""
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        try:
            self.cursor.execute("""
                INSERT INTO contas (cpf, titular, agencia, numero_conta, senha_hash, saldo)
                VALUES (?, ?, ?, ?, ?, 0.0)
            """, (cpf, titular, agencia, numero_conta, senha_hash))
            self.conexao.commit()
            print("✅ Conta criada com sucesso!")
        except sqlite3.IntegrityError:
            print("❌ Já existe uma conta com este CPF.")

    def autenticar(self, cpf, senha):
        """Verifica se a senha está correta."""
        self.cursor.execute("SELECT senha_hash FROM contas WHERE cpf=?", (cpf,))
        resultado = self.cursor.fetchone()
        if resultado:
            senha_hash = resultado[0]
            if bcrypt.checkpw(senha.encode(), senha_hash):
                print("✅ Login bem-sucedido!")
                return True
        print("❌ CPF ou senha incorretos.")
        return False

    def consultar_dados(self, cpf):
        self.cursor.execute("SELECT * FROM contas WHERE cpf=?", (cpf,))
        conta = self.cursor.fetchone()
        if conta:
            print("\n=== Dados da Conta ===")
            print(f"Titular: {conta[1]}")
            print(f"CPF: {conta[0]}")
            print(f"Agência: {conta[2]}")
            print(f"Número da Conta: {conta[3]}")
            print(f"Saldo: R$ {conta[5]:.2f}")
            print("======================")
        else:
            print("Conta não encontrada.")

    def depositar(self, cpf, valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        self.cursor.execute("UPDATE contas SET saldo = saldo + ? WHERE cpf=?", (valor, cpf))
        self._registrar_transacao(cpf, "Depósito", valor)
        self.conexao.commit()
        print(f"💰 Depósito de R$ {valor:.2f} realizado!")

    def sacar(self, cpf, valor):
        self.cursor.execute("SELECT saldo FROM contas WHERE cpf=?", (cpf,))
        saldo = self.cursor.fetchone()
        if not saldo:
            print("Conta não encontrada.")
            return
        if valor > saldo[0]:
            print("Saldo insuficiente.")
            return
        self.cursor.execute("UPDATE contas SET saldo = saldo - ? WHERE cpf=?", (valor, cpf))
        self._registrar_transacao(cpf, "Saque", valor)
        self.conexao.commit()
        print(f"💸 Saque de R$ {valor:.2f} realizado!")

    def _registrar_transacao(self, cpf, tipo, valor):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO transacoes (cpf, tipo, valor, data) VALUES (?, ?, ?, ?)",
                            (cpf, tipo, valor, data))
        self.conexao.commit()

    def ver_extrato(self, cpf):
        print("\n=== Extrato da Conta ===")
        self.cursor.execute("SELECT tipo, valor, data FROM transacoes WHERE cpf=? ORDER BY data DESC", (cpf,))
        transacoes = self.cursor.fetchall()
        for tipo, valor, data in transacoes:
            print(f"{data} - {tipo}: R$ {valor:.2f}")
        print("========================")
