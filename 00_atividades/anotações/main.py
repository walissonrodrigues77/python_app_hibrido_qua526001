import os
import time
import re

# Função para coletar os dados do usuário
dados_usuario = {}

# Limpando o terminal
os.system("cls" if os.name == "nt" else "clear")

# Função para validar o CPF no formato XXX.XXX.XXX-XX
def validar_cpf(cpf):
    # Expressão regular para CPF com máscara
    padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao_cpf, cpf))

# Função para validar o telefone no formato (DDD) NNNNN-NNNN
def validar_telefone(telefone):
    # Expressão regular para telefone com máscara
    padrao_telefone = r"^\(\d{2}\) \d{5}-\d{4}$"
    return bool(re.match(padrao_telefone, telefone))

# Coletando os dados
dados_usuario["nome"] = input("Digite seu nome: ")
dados_usuario["email"] = input("Digite seu e-mail: ")

# Coletando o telefone com máscara (DDD) NNNNN-NNNN
while True:
    telefone = input("Digite seu telefone: ")
    if validar_telefone(telefone):
        dados_usuario["telefone"] = telefone
        break
    else:
        print("Formato de telefone inválido. Tente novamente.")

# Coletando o CPF com máscara XXX.XXX.XXX-XX
while True:
    cpf = input("Digite seu CPF: ")
    if validar_cpf(cpf):
        dados_usuario["cpf"] = cpf
        break
    else:
        print("Formato de CPF inválido. Tente novamente.")

# Coletando o gênero
dados_usuario["genero"] = input("Digite seu gênero: ")

# Exibindo os dados armazenados no dicionário
time.sleep(2)
print("\nDados do usuário armazenados:\n")
for chave, valor in dados_usuario.items():
    time.sleep(1)
    print(f"{chave.capitalize()}: {valor}\n")
