import os 

from classes import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()
def main():

    usuario = PessoaFisica(
        nome="", 
        idade=0, 
        cpf="", 
        profissao="", 
        email="", 
        telefone="", 
        endereco="", 
    )
    empresa = PessoaJuridica(
        nome_fantasia="", 
        cnpj="", 
        website="", 
        email="",
        telefone="", 
        endereco="",  

    )
 
    print ("iNFORME OS DADOS DO USUÁRIO:\n")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").strip())
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.profissao = input("Informe a profissão: ").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereço: ").strip().title()




    print ("\nINFORME OS DADOS DA EMPRESA:\n")

    empresa = PessoaJuridica(


        nome_fantasia = input("Informe o nome da Empresa: ").strip().title(),
        cnpj = input("Informe o CNPJ da Empresa: ").strip(),
        website = input("Informe o website da Empresa: ").strip(),
        email = input("Informe o e-mail da Empresa: ").strip().lower(),
        telefone = input("Informe o telefone da Empresa: ").strip(),
        endereco = input("Informe o endereço da Empresa: ").strip().title(),
        
     )


    limpar()
    print(usuario)
    print(empresa)
    
if __name__ == "__main__":
    main()