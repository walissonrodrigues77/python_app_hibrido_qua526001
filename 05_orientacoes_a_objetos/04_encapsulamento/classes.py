class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__idade__ = cpf

 
    # método get
    @property
    def nome(self):
        return self.__nome
    
    # método ste (atribui valor)
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
      return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
        