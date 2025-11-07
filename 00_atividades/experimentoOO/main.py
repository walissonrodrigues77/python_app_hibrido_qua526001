from experimentoOO.classe import Banco

def main():
    banco = Banco()

    while True:
        print("\n=== Banco GPT 3.0 ===")
        print("1 - Criar conta")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            titular = input("Titular: ")
            cpf = input("CPF: ")
            agencia = input("Agência: ")
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            banco.criar_conta(titular, cpf, agencia, numero_conta, senha)

        elif opcao == "2":
            cpf = input("CPF: ")
            senha = input("Senha: ")
            if banco.autenticar(cpf, senha):
                menu_conta(banco, cpf)
        elif opcao == "3":
            print("👋 Obrigado por usar o Banco GPT!")
            break
        else:
            print("Opção inválida!")

def menu_conta(banco, cpf):
    while True:
        print("\n=== Menu da Conta ===")
        print("1 - Consultar dados")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Extrato")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            banco.consultar_dados(cpf)
        elif opcao == "2":
            valor = float(input("Valor do depósito: "))
            banco.depositar(cpf, valor)
        elif opcao == "3":
            valor = float(input("Valor do saque: "))
            banco.sacar(cpf, valor)
        elif opcao == "4":
            banco.ver_extrato(cpf)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
