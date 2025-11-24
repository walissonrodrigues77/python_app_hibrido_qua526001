import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o gênero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
        nascimento = datetime.strftime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado com sucesso."

        else:
            # instancia do objeto
            nova_pessoa = Pessoa(
                nome=nome,            
                nascimento=nascimento,
                email=email,
                genero=genero,
            )
            # insert into pessoa
            session.add(nova_pessoa)
            session.commit()

            return f"{nova_pessoa.nome} cadastrada com sucesso."

    except Exception as e:
        print(f"não foi possível cadastrar. {e}.")


def listar(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("\nPessoas cadastradas:\n")
        for pessoa in pessoas:

            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Gênero: {pessoa.genero}")
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
            print(f"\n{'-'*40}\n")
    except Exception as e:
        print(f"não foi possível listar. {e}.")
 

# update
def atualizar(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email = ""
    novo_nascimento = ""
    novo_genero = ""

    try:
    
        print("\nEscolha a pessoa que deseja alterar:\n")
        print("1 - ID")
        print("2 - e-mail")
        print("3 - retornar")     
        opcao = input("Opção desejada: ").strip()
        limpar()
       
       
        match opcao:
            case "1":
                id_pessoa = int(input("Informe o ID da pessoa: ").strip())
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail da pessoa: ").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return
            case _:
                return "Opção inválida."
            
        if pessoa:
            limpar()
            while True:
                print(f" ID {pessoa.id_pessoa}")
                print("Qual campo deseja alterar:\n")
                print(f"1 - Nome:{pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.nascimento.stfrtime("%d/%m/%Y")}")
                print(f"4 - Gênero: {pessoa.genero}")
                print(f"5 - Retornar ao menu principal")
                campo = input("Opção desejada: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower() 
                        pessoas = session.query(Pessoa).filter(Pessoa.email.like(novo_email)).all()
                        if novo_email in [pessoa.email for pessoa in pessoas]:
                            print("E-mail já cadastrado.")
                            continue
                        
                    case "3":
                        novo_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        novo_nascimento = datetime.strptime(novo_nascimento, "%d/%m/%Y").date()

                    case "4":
                        novo_genero = input("Informe o novo gênero: ").strip()

                    case "5":
                        novo_nome = novo_nome if novo_nome else pessoa.nome
                        novo_email = novo_email if novo_email else pessoa.email
                        novo_nascimento = datetime.strptime(novo_nascimento, "%d/%m/%Y").date() if novo_nascimento else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero else pessoa.genero
                        break
                    case _:
                        print("Opção inválida.")
                        continue

            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero
            session.commit()
            return "Dados alterados com sucesso."
        else:
            return "Pessoa não encontrada."
        
    except Exception as e:
        print(f"Não foi possível alterar os dados. {e}.")

def deletar(session, Pessoa):
    id_pessoa = ""
    email = ""
    pessoa = ""

    print("Informe o campo que deseja pesquisar:")
    print("1 - ID")
    print("2 - E-mail")
    print("Retornar")
    opcao = input("Informe o campo que deseja pesquisar: ").strip()  
    limpar()
    match opcao:
        case "1":
            id_pessoa = input("informe o ID a ser excluído:").strip()
            pessoa = session.query(Pessoa).flter_by(id_pessoa).first()
        case "2":
            email = input("Informe o e-mail do cadastro a ser excluído: ").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first()
        case "3":
            return ""
        case _:
            return "Opção inválida."
        
    if pessoa:
     limpar()
     print(f"ID: {pessoa.id_pessoa}")
     print(f"Nome: {pessoa.nome}")
     print(f"E-mail: {pessoa.email}")
     print(f"Gênero: {pessoa.genero}")
     print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%y")}")
     print({'-'*40})
     print("1 - Sim")
     print("2 - Não") 
     excluir = input("Tem certeza de que deseja excluir o registro? ").strip()
     match excluir:
         case "1":
             session.delete(pessoa)
             session.commit()
             return "Pessoa excluída com sucesso."
         case "2":
             return ""
         case _:
             return "Opção inválida."
     
