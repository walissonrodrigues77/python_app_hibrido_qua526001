# biblioteca
import os
import math

def limpar():
    os.system("cls")

    # funções de calculo
def quadrado(l):
        return l**2
    
def retangulo(b,h):
        return b*h
    
def triangulo(b, h):
            return (b*h)/2
     # Importamos a biblioteca math para usar a função sqrt (raiz quadrada)

def calcular_hipotenusa(cateto1, cateto2):
    """Calcula a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras."""
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return hipotenusa

    
    
limpar()

while True:
    print("1 - calcular quadrado")
    print("2 - calcular retângulo")
    print("3 - calcular triângulo")
    print("4 - calcular hipotenusa")
    print("5 - sair do programa")
    opcao = input("\nOpção desejada:").strip()
    limpar()
    match opcao:
        case "1":
          l = float(input("informe o lado do quadrado: ").strip().replace(",","."))
          resultado = quadrado(l)
          limpar()
          print(f"Area do quadrado: {resultado}")
          continue
        case "2":
          b = float(input("Informe a base do retângulo").strip().replace(",","."))
          h = float(input("Informe a altura do retângulo").strip().replace(",","."))
          resultado = retangulo(b,h)
          limpar()
          print(f"Área do retângulo: {resultado}")
          continue
        case "3":
          b = float(input("Informe a base do triângulo: ").strip().replace(",","."))
          h = float(input("Informe a base  do triângulo: ").strip().replace(",","."))
          continue
        case "4":
                cat1 = float(input("Digite o valor do primeiro cateto: ")).strip().replace(",",".")
                cat2 = float(input("Digite o valor do segundo cateto: ")).strip().replace(",",".")
                resultado = calcular_hipotenusa(cat1, cat2)
                print(f"A hipotenusa é: {resultado:.2f}")

                continue
        case "5":
              break
        case _:
           print("programa encerrado.\n")
           continue
