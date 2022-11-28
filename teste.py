from datetime import datetime

class Pessoa:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__nascimento = datetime.now()

    @property
    def name(self):
        return self.__nome
    
    @name.setter
    def name(self, nomes):
        self.__nome = nomes

p1 = Pessoa('Guilherme')
print(p1.name)
p1.name = "Guui"
print(p1.name)