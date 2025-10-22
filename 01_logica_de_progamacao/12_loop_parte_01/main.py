# tramento de exceção
try:
    # entrada de dados
    numero = int(input("Informe um número inteiro:").strip())
    
    # laço de reptição
    while numero >= 0:
        print(numero)
        numero -=1 
except:
    print("Nao foi possível executar o contador.")