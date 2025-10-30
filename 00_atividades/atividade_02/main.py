

#Crie um programa que receba um número inteiro do usuário,
#e mostre uma contagem em regressiva em segundos,
#e ao terminar, exiba uma mensagem qualquer.

import time
import os
# tramento de exceção
try:
    # entrada de dados
    numero = int(input("Informe um número:").strip())
    os.system("cls")
    
    # laço de reptição
    while numero >= 0:
        time.sleep(1)
        print(numero)
        time.sleep(1)
        numero -=1
        os.system("cls")

    # mensagem final
    print("Obrigado volte Sempre. ")
    time.sleep(2)

except:
    print()