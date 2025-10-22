# tratamento de exceção
try:
    # entrda de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input(" Informe sua idade: ").strip())
    altura = float(input("Informe sua altura: ").strip().replace(",","."))

    # saída de dados
    print(f"nome: {nome}") 
    print(f"Idade: {idade}") 
    print(f"Altura: {Altura}") 
    pass
except:
    print("infelizmente o programa não pode ser executado.")
