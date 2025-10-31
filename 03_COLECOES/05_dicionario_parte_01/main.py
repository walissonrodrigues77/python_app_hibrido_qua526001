# declaração de dicionário
import time
import os
usuario = {
    'nome': "Walisson rodrigues",
    'idade': 35,
    'peso': 75.1,
    'altura': 1.71,
    'email': "walissongmail.com"
}
time.sleep(2)
os.system("cls")

print(f"Nome: {usuario['nome']}")
time.sleep(1)
print(f"Idade: {usuario['idade']}")
time.sleep(2)
print(f"peso: {usuario['peso']}")
time.sleep(2)
print(f"Altura: {usuario['altura']}")
time.sleep(2)
print(f"e-mail: {usuario['email']}\n")