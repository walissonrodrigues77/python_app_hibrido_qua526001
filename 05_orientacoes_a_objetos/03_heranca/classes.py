class Pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone
    
    def exibir_dados(self):
        print(f"E_mail: {self.email}")
        print(f"telefone: {self.telefone}")
                    



class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, idade, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email=email, telefone=telefone)
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, telefone=telefone)

    def exibir_dados(self):
        print(f"Nome_fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()


    
    
    
    


    

