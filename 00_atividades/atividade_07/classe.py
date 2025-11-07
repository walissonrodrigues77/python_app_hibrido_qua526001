class Conta:
    def __init__(self, titular, cpf, agencia, numero_conta, saldo=0.0):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def consultar_dados(self):
        print("\n=== Dados da Conta ===")
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("======================")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
