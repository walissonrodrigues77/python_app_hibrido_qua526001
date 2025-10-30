"""
Crie um programa que receba do usuário o nome, e-mail, cpf e telefone, limpe o console, e em seguida, exiba as informações do usuário na tela.
"""
import os

# inputs resolvido 

nome = input("Informe seu Nome.").strip().title() #string
email = input("Informe seu E-mail. ").strip().lower()#string
cpf = input("Informe seu CPF. ").strip() #string
telefone = input("Informe seu Número. ").strip()#string
 
os.system("cls")
print(f"Olá, meu nome é {nome}."),
print(f"o meu E-mail é o: {email}.")
print(f"e meu telefone é o: {telefone}.")