class Carro:

    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca    
        self.modelo = modelo  
        self.ano = ano        
        self.cor = cor        

carro1 = Carro("Toyota", "Corolla", 2020, "Prata")
carro2 = Carro("Honda", "Civic", 2022, "Preto")
carro3 = Carro("Fiat", "Argo", 2024, "Branco")
carro4 = Carro("Volkswagen", "Polo", 2025, "Vermelho")
carro5 = Carro("Chevrolet", "Onix", 2021, "Azul")

print(f"Carro 1: {carro1.marca}, {carro1.modelo}, {carro1.ano}, {carro1.cor}")
print(f"Carro 2: {carro2.marca}, {carro2.modelo}, {carro2.ano}, {carro2.cor}")
print(f"Carro 3: {carro3.marca}, {carro3.modelo}, {carro3.ano}, {carro3.cor}")
print(f"Carro 4: {carro4.marca}, {carro4.modelo}, {carro4.ano}, {carro4.cor}")
print(f"Carro 5: {carro5.marca}, {carro5.modelo}, {carro5.ano}, {carro5.cor}")
