from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    valor = 0.0

    def __init__(self, valor_compra):
        # Atribuição da auto-referência
        self.valor = valor_compra
    
    @abstractmethod
    def pagar(self):
        pass

class CartaoCredito(MetodoPagamento):

    def pagar(self):
        acrescimo = self.valor * 0.05
        valor_final = self.valor + acrescimo
        
        print("\n--- Método: Cartão de Crédito ---")
        print(f"Valor Original: R$ {self.valor:.2f}")
        print(f"Acréscimo (5%): R$ {acrescimo:.2f}")
        print(f"Valor Final a Pagar: R$ {valor_final:.2f}")

class BoletoBancario(MetodoPagamento):

    def pagar(self):
        desconto = self.valor * 0.02
        valor_final = self.valor - desconto
        
        print("\n--- Método: Boleto Bancário ---")
        print(f"Valor Original: R$ {self.valor:.2f}")
        print(f"Desconto (2%): R$ {desconto:.2f}")
        print(f"Valor Final a Pagar: R$ {valor_final:.2f}")

class Pix(MetodoPagamento):

    def pagar(self):
        valor_final = self.valor 

        print("\n--- Método: Pix ---")
        print(f"Valor Original: R$ {self.valor:.2f}")
        print("Acréscimos/Descontos: Não há")
        print(f"Valor Final a Pagar: R$ {valor_final:.2f}")

valor_compra = float(input("Digite o valor total da compra: R$ "))

print("\nEscolha o método de pagamento:")
print("1 - Cartão de Crédito (Acréscimo 5%)")
print("2 - Boleto Bancário (Desconto 2%)")
print("3 - Pix (Sem alteração)")
escolha = input("Digite o número da sua escolha (1, 2 ou 3): ")

metodo_escolhido = None 

if escolha == '1':
    metodo_escolhido = CartaoCredito(valor_compra)
elif escolha == '2':
    metodo_escolhido = BoletoBancario(valor_compra)
elif escolha == '3':
    metodo_escolhido = Pix(valor_compra)
else:
    print("Escolha inválida. O pagamento não foi processado.")

if metodo_escolhido:

    metodo_escolhido.pagar()

""" RESPOSTA: O Polimorfismo facilitou porque o código que processa o código não precisa saber qual é o TIPO exato de pagamento. O sistema apenas sabe que o objeto está na variável.As vantagens de usar uma interface abstrata é a garantia de que toda classe de pagamento é implementada no métod essencial."""