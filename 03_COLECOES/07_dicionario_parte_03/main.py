# declaração de dicionario
import os
import time
veiculo = {
'fabricante': "Chevrollet",
'modelo': "chevete",
'ano': 1973,
'cor': "branco",
'placa': "df-1973"

}
os.system("cls")
# exibir os dados 
for chave in veiculo:
    time.sleep(1)
    print(f"{chave.capitalize()}: {veiculo[chave]}")


    # usuario escolhe o campo que deseja mudar

while True:
    campo = input("\nInforme o nome do campo que deseja alterar ou digite 'sair' para encerrar o programa: ").strip().lower()

    match campo:
         case "fabricante":
            veiculo['fabricante'] = input("Informe o novo valor de 'fabricante'").strip()
            
         case "modelo":
            veiculo['modelo'] = input("Informe o novo valor de 'modelo'").strip()
            
         case "ano":
            veiculo['ano'] = input("Informe o novo valor de 'ano'")
            
         case "cor":
            veiculo['cor'] = input("Infrome o novo valor de 'cor'")
            
         case "placa":
            veiculo['placa'] = input("Informe o novo valor de placa\n'")
         case "sair":
            break
         case _:
          print("valor invalido.")
          continue
# Mostra na tela os novo valores
for chave in veiculo:
  print(f"{chave.capitalize()}:{veiculo[chave]}")


