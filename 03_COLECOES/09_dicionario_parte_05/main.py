# bibliotecas
import os
import time

# Declaração de lista
usuarios = []
os.system("cls")

# limpa console (não é ideal usar "cls" diretamente, mas para o seu exemplo funciona)
# os.system("cls") # Melhor limpar dentro do loop ou função

while True:
    # Tudo abaixo desta linha deve estar indentado com 4 espaços para fazer parte do loop
    
    # menu (agora parte do loop, será exibido toda vez)
    print("1 - Cadastrar novo usuário: ") # Corrigi para 'usuário' singular
    print("2 - Listar usuários: ")
    print("3 - Sair do programa: ")
    
    opcao = input("Informe a opção desejada: ").strip()
    # os.system("cls") # Limpar a tela aqui ou dentro dos cases é uma boa prática
    
    match opcao:
        # Tudo abaixo desta linha deve estar indentado com 4 espaços a mais (total de 8)
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o novo nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuário: ").strip())
            # CORREÇÃO: E-mail deve ser string, não int. lower precisa de parênteses.
            usuario['email'] = input("Informe o e-mail do usuário: ").strip().lower() 
            # CORREÇÃO: Você precisa adicionar o dicionário à lista aqui!
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuário inserido com sucesso.") 
        
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                   print(f"{chave.capitalize()}:{usuario[chave]}")
                print(f"{'-'*40}")
    
        
        case "3":
            print("\nSaindo em 3.")
            time.sleep(3)
            os.system("cls")
            print("\nSaindo em 2.")
            time.sleep(2)
            os.system("cls")
            print("\nSaindo em 1.\n ")
            time.sleep(1)
            os.system("cls")
            print("\nPrograma encerrado!\n ")
            break # Interrompe o loop 'while True'
        
        case _:
            print("\n((((Opção inválida))))\n")
            continue # Volta para o início do loop 'while True'
