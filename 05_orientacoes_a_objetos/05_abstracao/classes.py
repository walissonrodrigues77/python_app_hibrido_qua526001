from abc import ABC, abstractmethod

class IParque(ABC):
    @abstractmethod
    def entrada_infantil(self):
        pass
    
    @abstractmethod
    def entrada_adolencentes(self):
        pass

    @abstractmethod
    def entrada_adultos(self):
        pass

# classe
class Parque(IParque):
    # construtor 
    def __init__(self, nome, idade, peso):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome 
    
    @nome.setter
    def nome(self):
        return self.__nome


    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def idade(self):
        return self.__idade


    @property
    def peso(self):
        return self.__peso

    @nome.setter
    def peso(self):
        return self.__peso



    def entrada_infantil(self):
        if self.idade <= 13 and self.peso < 70:
            return f"Ingresso liberado para {self.__nome}."
        else:
            return f"Entrda Proibida para {self.__nome}."
        
    def entrada_adolencentes(self):
        if 13 <= self.__idade <= 17 and self.__peso <= 80:
            return f"Ingresso adolescente liberado para {self.__nome}!"
        else:
            return f"Entrada adolescente proibida para {self.__nome}."

    def entrada_adultos(self):
        if self.__idade >= 18 and self.__peso <= 120:
            return f"Ingresso adulto liberado para {self.__nome}!"
        else:
            return f"Entrada adulta proibida para {self.__nome}."
        
        