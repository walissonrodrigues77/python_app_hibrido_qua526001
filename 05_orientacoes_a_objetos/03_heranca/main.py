# bibliotecas do python
import os
# nossa biblioteca 
from classes import PessoaFisica, PessoaJuridica
 
# função limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# funções principal
def main():
    usuario = PessoaFisica(nome="", cpf="", idade=0, email="", telefone="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", email="",)

 # menu
    limpar()
    while True:
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados da Empresa")
        print("3 - Exibir dados do Usuário")
        print("4 - Inserir dados da Empresa")
        print("5 - Sair do programa")
        opcao = input("Opção desejada: ").strip()

        match opcao:
     
            case "1":
                usuario.nome = input("Informe seu nome:").sprip().title()
                usuario.cpf = input("Informe seu cpf:").strip()
                usuario.idade = input("Informe sua idade").strip()
                usuario.email = input("Informe seu e-mail").strip().lower()
                usuario.telefone = input("Informe seu telefone").strip()
                continue
            case "2":
                empresa.nome_fantasia = input("Informe o nome da Empresa").strip().title()
                empresa.cnpj = input("Informe o CNPJ").strip()
                empresa.email = input("Informe o e-mail").strip().lower()
                empresa.telefone = input("Informe o telefone da empresa:").strip()
                continue
            case _:
               
              break
      
    
if __name__ == "__main__":
    main()
