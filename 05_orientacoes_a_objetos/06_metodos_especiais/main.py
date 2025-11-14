import os

from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pessoa = Pessoa(nome="", idade=0, genero="", telefone="")

    pessoa.nome = input("Informe o nome: ").strip().title()
    pessoa.idade = int(input("Informe a idade: ").strip())
    pessoa.genero = input("Informe o gênero: ").strip().lower()
    pessoa.telefone = input("Informe o telefone: ").strip()

    # saída de dados
    print(pessoa)
    print(f"Idade: {len(pessoa)}")

if __name__ == "__main__":
    main()