class Pessoa:
    # construtor
    def __init__(self, nome, idade, genero, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        self.__telefone = telefone
    
    # métodos especiais
    def __str__(self):
        return f"Olá, meu nome é {self.__nome}, tenho {len(self)} anos, sou do gênero {self.__genero} e meu telefone é {self.__telefone}."
    
    def __len__(self):
        return self.__idade
    
    # métodos set e get
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone