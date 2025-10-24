# TODO: atividade

#Crie um programa que receba do usuário o nome,
#  peso (em kg) e altura (em metros), 
# calcule o IMC do usuário (arredondado para 2 casas decimais),
#  e exiba o diagnóstico do usuário com base na tabela do IMC.
import math
import os
import time


nome = input("Informe seu nome: ")
peso = float(input("Informe seu peso: ").strip().replace(",","."))
altura = float(input("Informe sua altura em metros: ").strip().replace(",","."))
os.system("cls")

# calcular imc
imc = peso/ (altura ** 2)
imc_arredondado = round(imc, 2)
                        
                        #exibir diagnostico
print(f"Nome: {nome}")
print(f"Seu imc é: {imc_arredondado}")
  
  
if imc < 18.5:
    print("Diagnostico:Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Diagnostico: peso normal:")
elif 24.9 <= imc < 29.9:
    print(f"Diagnostico: Sobrepeso:")
else :
    print("Diagnostico: Obesidade:")
    
time.sleep(3)


print(" Programa finalizado Volte sempre:")