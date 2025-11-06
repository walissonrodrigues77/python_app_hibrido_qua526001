class Pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, idade, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email=email, telefone=telefone)

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia = nome_fantasia):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email, telefone=telefone)

    

