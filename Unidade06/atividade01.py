class Veiculo:
    total_veiculos = 0

    def __init__(self, placa, modelo, diaria):
        self.__placa = placa       
        self.__alugado = False        
        self.modelo = modelo         
        self.diaria = diaria         

        Veiculo.total_veiculos += 1
        print(f"Veículo {self.modelo} ({self.__placa}) cadastrado.")

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, nova_placa):
    
        print(f"\nA placa do veículo ({self.__placa}) não pode ser modificada!")

    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"Veículo {self.modelo} foi alugado com sucesso.")
        else:
            print(f"Veículo {self.modelo} já está alugado.")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"Veículo {self.modelo} foi devolvido e está disponível.")
        else:
            print(f"Veículo {self.modelo} já está disponível.")

    def status(self):
        estado = "Alugado" if self.__alugado else "Disponível"
        print(f"Status: {self.modelo} ({self.__placa}) está: {estado}")

    @classmethod
    def mostrar_total_veiculos(cls):

        print(f"\nTotal de veículos cadastrados no sistema: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        
        valor_total = dias * diaria
        return valor_total

veiculo1 = Veiculo(placa="ABC1234", modelo="Fiat Uno", diaria=50.00)
veiculo2 = Veiculo(placa="XYZ5678", modelo="Toyota Corolla", diaria=150.00)

Veiculo.mostrar_total_veiculos()
print("-" * 50)

print("\nTentando alugar o Veículo 2:")
veiculo2.alugar()
veiculo2.status()

print("\nDevolvendo o Veículo 2:")
veiculo2.devolver()
veiculo2.status()

print(f"A placa do Veículo 1 é: {veiculo1.placa}")

veiculo1.placa = "DEF9999"

print(f"A placa do Veículo 1 após tentativa de mudança continua sendo: {veiculo1.placa}")

dias_aluguel = 7
print(f"\nCálculo do aluguel do Veículo 1 ({veiculo1.modelo}) por {dias_aluguel} dias:")

preco_final = Veiculo.calcular_preco_aluguel(dias=dias_aluguel, diaria=veiculo1.diaria)

print(f"Diária: R$ {veiculo1.diaria:.2f}")
print(f"O valor total do aluguel é: R$ {preco_final:.2f}")

