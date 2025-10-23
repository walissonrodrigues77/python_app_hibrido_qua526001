# biblioteca
import os
import math

os.system("cls")

# entrada de dados
r = float(input("Informe o raio do circulo: ").strip().replace(",","."))

# calculos
a = math.pi*(r**2)
c = 2*math.pi*r

#saida de dados
print(f"Número do pi: {math.pi}")
print(f"Área da circunferência: {a:.2f}")
print(f"Tamanho da circumferência: {c:.2f}")

