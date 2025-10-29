# bibliotecas
import os



# declaração de lista 
nomes = []


# Limpa o cosele
os.system("cls")


#loop
while True:
#Menu
    print("1 - Inserir novo nome")
    print("2 - Exibir lista de nomes")
    print("3 - Excluir nome na lista")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    match opcao:
        case "1":
            os.system("cls")
            novo_nome = input("Informe o novo nome: ").strip().title()
            nomes.append(novo_nome) # isere novo nome na lista
            os.system("cls")
            print(f"{novo_nome} cadastro iserido com sucesso.")
            continue
        case "2":
            os.system("cls")
            print("Lista de nomes:\n")
            for i in range(len(nomes)):
                print(f"{i} - {nomes[i]}")
                print(f"\n{'-'*40}\n")
                continue
        case "3":
             os.system("cls")
             try:
              posicao = int(input("informe a posição a ser excluida: ").strip())
              if posicao >=0 and posicao < len(nomes):
                  del(nomes[posicao])
                  print("Nome excluído com sucesso.")
                  
              else:
                  print("Posição inexistente.")
             except Exception as e:
                print(f"Posição inválida.{e}.")
             continue            
        case "4":
           print("Programa encerrado.")
           pass
           break
        case _:
            print("Programa ")
            continue

