from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from entidades import criar_tb_pessoa
from modulo import limpar, cadastrar, listar, atualizar

def main():
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()


    limpar()

    while True:
        print(f"\n{'-'*20} 😈 CRUD DA COBRA 🐍{'-'*20}\n")
        print("0 - Sair do Programa")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas ")
        print("3 - Atualizar dados de uma pessoa")
        

        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "0":
                print("\nPrograma encerrado...\n")
                break

            case "1":
                cadastrar(session, Pessoa)
                continue

            case "2":
                listar(session, Pessoa)
                continue

            case "3":
                atualizar(session, Pessoa)
                continue


            case _:
                print("Opção inválida.")
                continue

    session.close()


if __name__ == "__main__":
    main()