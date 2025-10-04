
from abc import ABC, abstractmethod

class CartaoWeb(ABC):

    destinatario = ""

    @abstractmethod
    def showMessage(self):
        pass

class DiaDosNamorados(CartaoWeb):

    def __init__(self, destinatario_nome):
        self.destinatario = destinatario_nome

    def showMessage(self):
        print("--- Cartão de Dia dos Namorados ---")
        print(f"Querido(a) {self.destinatario},")
        print("Neste dia especial, meu amor por você só cresce! Feliz Dia dos Namorados!")

class Natal(CartaoWeb):

    def __init__(self, destinatario_nome):
        self.destinatario = destinatario_nome

    def showMessage(self):
        print("--- Cartão de Natal ---")
        print(f"Olá {self.destinatario},")
        print("Que a magia do Natal traga muita paz, alegria e prosperidade para você e sua família. Feliz Natal!")

class Aniversario(CartaoWeb):

    def __init__(self, destinatario_nome):
        self.destinatario = destinatario_nome

    def showMessage(self):
        print("--- Cartão de Aniversário ---")
        print(f"Parabéns {self.destinatario}!")
        print("Que seu novo ciclo seja repleto de realizações, saúde e sucesso. Muitas felicidades!")


print("--- Simulação de Cartões Web ---")

cartao_namorados = DiaDosNamorados("Maria")
cartao_natal = Natal("João")
cartao_aniversario = Aniversario("Pedro")
cartao_generico = None

print("\n--- TESTE 1: Cartão Dia dos Namorados ---")
cartao_generico = cartao_namorados

cartao_generico.showMessage()

print("\n--- TESTE 2: Cartão Natal ---")
cartao_generico = cartao_natal

cartao_generico.showMessage()

print("\n--- TESTE 3: Cartão Aniversário ---")
cartao_generico = cartao_aniversario

cartao_generico.showMessage()

""" Resposta: O polimorfismo ocorre no código de maneira que
uma única instrução produz resultados diferentes, dependendo do TIPO de objeto que a variável está referenciando naquele momento.
"""