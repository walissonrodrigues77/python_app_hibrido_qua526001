# biblioteca
import os

# classe
class Pessoa:
    # atributos 
    nome = "Walisson Rodrigues"
    idade = 35
    email = "walisson@gmail.com"

    # métado
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}\n")

if __name__ == "__main__":
    # instancia a classe (cria novo objeto
    usuario = Pessoa()

    # limpa console
    os.system("cls" if os.name == "nt" else "clear")

    # saída de dados
    usuario.exibir_dados()
    