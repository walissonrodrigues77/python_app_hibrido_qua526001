# funções

import os
def boas_vindas(nome):
  print(f"\n😂  Seja bem vindo, {nome} ❤\n")


    # algoritmo principal
os.system("cls")
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)