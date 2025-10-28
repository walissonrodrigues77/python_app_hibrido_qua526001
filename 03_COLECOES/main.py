# declaração de lista
nomes = []

try: 
     while True:
        print("1 - Inserir nome na lista")
        print("2 - Exibir lista")
        print("3 - Sair do Programa")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                novo_nome = input("Informe o novo nome:\n").strip().title()
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!\n")
    
            case "2":
                print("\nLista de nomes:\n")
                for nome in nomes:
                    print(nome)
            case "3":
                break
            case _:
                print("opção inválida")
                continue



except Exception as e:

    print(f"Erro ao exibir a lista. {e}.")

finally:
    print(f"programa Encerrado ...")