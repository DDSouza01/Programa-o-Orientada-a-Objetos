
class Restaurante:

    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nome = nomeRestaurante
        self.cozinha = tipoCozinha

    def descreverRestaurante(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo de Cozinha: {self.cozinha}")

    def abrirRestaurante(self):
        print(f"Restaurante {self.nome} está aberto!")

    def __str__(self):
        return f"Nome: {self.nome} | Cozinha: {self.cozinha}"

restaurante_a = Restaurante("Zé da Buchada", "Cearense")

restaurante_b = Restaurante("Espetinho do Paulo", "Cearense")

restaurante_c = Restaurante("Churrasco da Tia Maria", "Cearense")

print("\n--- Restaurante A ---")
restaurante_a.descreverRestaurante()

print("\n--- Restaurante B ---")
restaurante_b.descreverRestaurante()

print("\n--- Restaurante C ---")
restaurante_c.descreverRestaurante()

restaurante_a.abrirRestaurante()
restaurante_b.abrirRestaurante()
restaurante_c.abrirRestaurante()

print("\nRestaurante A (via __str__):")
print(restaurante_a)

print("\nRestaurante B (via __str__):")
print(restaurante_b)

print("\nRestaurante C (via __str__):")
print(restaurante_c)
