import os
from classes import Parque

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # Criando o objeto ingresso
    ingresso = Parque(nome="", idade=0, peso=0.0)

    # Coletando informações do usuário
    ingresso.nome = input("Informe o nome: ").strip().title()
    ingresso.idade = int(input("Informe a idade: ").strip())
    ingresso.peso = float(input("Informe o peso em Kg: ").strip().replace(",", "."))

    limpar()

    while True:
        # Mostrando o menu
        print("1 - Categoria Infantil")
        print("2 - Categoria Adolescente")
        print("3 - Categoria Adulto")
        print("4 - Sair do programa")
        opcao = input("Opção desejada: ").strip()

        # Estrutura de decisão (match-case Python 3.10+)
        match opcao:
            case "1":
                print(ingresso.entrada_infantil())
            case "2":
                print(ingresso.entrada_Adolecente())
            case "3":
                print(ingresso.entrada_adulto())
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida")

if __name__ == "__main__":
    main()
