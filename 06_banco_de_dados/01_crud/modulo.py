import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o gênero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

        if email in {pessoa.email for pessoa in session.query(Pessoa).all()}:
            return "E-mail já cadastrado com sucesso."

        else:
            nova_pessoa = Pessoa(
                nome=nome,            
                nascimento=nascimento,
                email=email,
                genero=genero,
            )
            session.add(nova_pessoa)
            session.commit()

            return f"Pessoa {nova_pessoa.nome} cadastrada com sucesso."

    except Exception as e:
        print(f"não foi possível cadastrar. {e}.")


    