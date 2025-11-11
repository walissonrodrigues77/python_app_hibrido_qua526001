from classes import Pessoa

def main():
    usuario = Pessoa(nome="", cpf="")

    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF").strip()

    print(f"Nome:{usuario.nome}")
    print(f"CPF:{usuario.cpf}")


if __name__ == "__main__":
    main()