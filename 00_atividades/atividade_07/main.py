# TODO: atividade
# criar um app de banco. o programa deverá ter a classe conta, com os atribtos:
# titular da conta (nome)
# cpf do titular
# numero da agencia
# numero da Conta
# saldo
# o usuario ira inserir os dados "titular da conta e cpf e poderar escolher entre as seguintes opções 
# consultar dados da conta 
# depositar valor
# sacar valor
# sair do programa
# #( em python com ) "

from experimentoOO.classe import Conta
import os
def main():
    print("=== Bem-vinndo ao Banco Python ===\n")

    titular = input("Digite o nome do titular da conta: ")
    cpf = input("Digite o CPF do titular: ")
    agencia = input("Digite o número da agência: ")
    numero_conta = input("Digite o número da conta: ")

    conta = Conta(titular, cpf, agencia, numero_conta)

    while True:
        print("\n=== Menu ===")
        print("1 - Consultar dados da conta")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta.consultar_dados()
        elif opcao == "2":
            valor = float(input("Digite o valor para depósito: "))
            conta.depositar(valor)
        elif opcao == "3":
            valor = float(input("Digite o valor para saque: "))
            conta.sacar(valor)
        elif opcao == "4":
            print("Saindo do sistema... Obrigado por usar o Banco Python!")
            break
        else:
            print("Opção inválida! Tente novamente.")
os.system("cls")
if __name__ == "__main__":
    main()
