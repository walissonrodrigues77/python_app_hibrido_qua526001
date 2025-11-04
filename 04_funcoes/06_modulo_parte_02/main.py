# função principal
def main():
# enttrada de dados 
   nome = input("Informe seu nome: ").strip().title()
   idade = int(input("Informe sua idade: ").strip())

    #operador ternario
                                          
   resultado = " vc é maior de idade." if idade >= 18 else " vc é menor de idade."

   # saida de dados 
   print(f"{nome}{resultado}")

   #protege algoritmo principal
if __name__ == "__main__":
   main()