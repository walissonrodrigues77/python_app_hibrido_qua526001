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



#Recomendação de crédito

#➡️ Aprendizado: Python é excelente pra isso — estude Machine Learning (bibliotecas como pandas, scikit-learn).


#Tokens de acesso

#➡️ Aprendizado: entenda criptografia básica e autenticação JWT.

#💬 3. Chatbots inteligent

#Fintechs usam IA (como eu 😄) para atender clientes automaticamente.

💡# Como fazer:
#Usar APIs de linguagem natural (NLP) — por exemplo:

#OpenAI API (para chatbots)

#Rasa (plataforma de chatbot open-source)
#Depois disso, estudar IA aplicada a dados financeiros

➡️ Sugestão de trilha:

#Etapa	Aprendizado
#1	Lógica e Python
#2	Programação orientada a objetos
#3	Banco de dados (SQLite, PostgreSQL)
#4	Criptografia e autenticação
#5	APIs e integração web
#6	Machine Learning (pandas, scikit-learn)
#7	Frameworks web (Flask, FastAPI)



#(rainbow tables).



#