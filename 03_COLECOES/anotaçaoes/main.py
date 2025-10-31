# bibliotecas
import os

# Declaração de lista
usuarios = []

# limpa console (não é ideal usar "cls" diretamente, mas para o seu exemplo funciona)
# os.system("cls") # Melhor limpar dentro do loop ou função

while True:
    # Tudo abaixo desta linha deve estar indentado com 4 espaços para fazer parte do loop
    
    # menu (agora parte do loop, será exibido toda vez)
    print("1 - Cadastrar novo usuário") # Corrigi para 'usuário' singular
    print("2 - Listar usuários")
    print("3 - Sair do programa")
    
    opcao = input("Informe a opção desejada: ").strip()
    # os.system("cls") # Limpar a tela aqui ou dentro dos cases é uma boa prática
    
    match opcao:
        # Tudo abaixo desta linha deve estar indentado com 4 espaços a mais (total de 8)
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o novo nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuário: ").strip())
            # CORREÇÃO: E-mail deve ser string, não int. lower precisa de parênteses.
            usuario['email'] = input("Informe o e-mail do usuário").strip().lower() 
            # CORREÇÃO: Você precisa adicionar o dicionário à lista aqui!
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuário inserido com sucesso.") 
        
        case "2":
            pass
        
        case "3":
            break # Interrompe o loop 'while True'
        
        case _:
            print("Opção inválida")
            continue # Volta para o início do loop 'while True'
