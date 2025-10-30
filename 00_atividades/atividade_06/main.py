# TODO: atividade
# """
# crie um programa que receba do usuario os seguintes dados:
# -nome
# -e-mail
# -telefone
# -cpf
# genero
# apos isso, o programa deve armazenar esses dados em um dicionário e exibir os dados desse dicionario n atela.
# """
import os
import time

  # Função para coletar os dados do usuário
dados_usuario = {}
os.system("cls")

    # Coletando os dados
dados_usuario["nome"] = input("Digite seu nome: ")
dados_usuario["email"] = input("Digite seu e-mail: ")
dados_usuario["telefone"] = input("Digite seu telefone: ")
dados_usuario["cpf"] = input("Digite seu CPF: ")
dados_usuario["genero"] = input("Digite seu gênero: ")

    # Exibindo os dados armazenados no dicionário
time.sleep(2)
print("\nDados do usuário armazenados:\n")
for chave, valor in dados_usuario.items():
  time.sleep(1)
  print(f"{chave.capitalize()}: {valor}\n")



