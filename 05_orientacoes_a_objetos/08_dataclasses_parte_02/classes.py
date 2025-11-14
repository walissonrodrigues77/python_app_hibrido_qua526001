from dataclasses import dataclass
@dataclass  
class Pessoa:
    email: str
    telefone: str
    endereco: str

    def __str__(self):
        return f" E-mail: {self.email}\nTelefone: {self.telefone}\n Endereço:{self.endereco}"
    
@dataclass
class PessoaFisica(Pessoa):
    nome: str
    idade: int
    cpf: str
    profissao: str

    def __str__(self):
        return f"\nDADOS DO USUÁRIO: \nNOME: {self.nome}\n Idade: {len(self)}\nCPF: {self.profissao}\n {super().__str__()}"
    
    def __len__(self):
        return self.idade
    
@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str
    
    def __str_(self):
        return f"\nDADOS DA EMPRESA: \nNOME DA EMPRESA: {self.nome_fantasia}\n CNPJ: {self.cnpj}\n Website:{self.website}\n{super().__init__()}"