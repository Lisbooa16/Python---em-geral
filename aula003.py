from typing import List, Tuple

#Encapsulamento

class Curso:
    def __init__(self: object, nome: str = "Curso Padrao", carga_horaria: int = 45) -> None:
        self.__nome = nome
        self.__carga = carga_horaria
    
curso1: Curso = Curso()
curso2: Curso = Curso(nome="Padroes de projetos em python curso 3")
curso3: Curso = Curso(nome="Orquestração de containers com Kubernets", carga_horaria=23)

# print(curso1.__dict__)
# print(curso2.__dict__)
# print(curso3.__dict__)

#Polimorfismo

nome: str = "Geek University"
tuple: Tuple = (1,2,3,4,5)
lista: List = [1,2,3,4,5]

# print(nome[:4], tuple[:4], lista[:4])

#Herança

class Pessoa:
    def __init__(self: object, nome: str) -> None:
        self.__nome = nome

    def andar(self:object) -> None:
        print('Estou andando.....')

class Aluno(Pessoa):
    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula


felicity = Aluno('Felicity', '12345')
# felicity.andar()

#Abstração
def gerar_fibonaci(qtd: int) -> None:
    if qtd <= 0:
        print('A quantidade deve ser maior que zero')
    else:
        print(f'a sequencia fibonaci para {qtd} termo(s) é: ')
        contador : int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1)
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1

# gerar_fibonaci(10)