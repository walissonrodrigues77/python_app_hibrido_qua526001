import os

from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="", idade=0, altura=0.0)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").strip())
    usuario.altura = float(input("Informe a altura em metros: ").strip().replace(",","."))

    limpar()
    print(usuario)
    print(f"{usuario.nome} {usuario.verificar_maioridade()}.")

if __name__ == "__main__":
    main()