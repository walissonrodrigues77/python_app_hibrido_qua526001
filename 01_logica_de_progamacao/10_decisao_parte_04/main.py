# declaração de variaveis 
x = float(input("informe o 1º número:").strip().replace(",","."))
y = float(input("informe o 2° número:").strip().replace(",","."))

# menu
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
operador = input("informe a operação desejada:").strip()

#decisão 
match operador:
     case "1":
          print(f"A soma é {x+y}")
     case "2":
          print(f" a subtração é {x-y}")
     case "3":
          print(f"a multplicação é {x*y}")
     case "4":
          print(f" a divisão é {x/y}")
     case _:
        print(" operação invalida.")

            