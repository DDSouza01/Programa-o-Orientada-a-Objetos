import datetime
import random

class Usuario:

    def __init__(self, rg=0, cpf=0, nome="Anonimo", dataNascimento=datetime.date(1900, 1, 1)):
        self._rg = rg                
        self._cpf = cpf
        self._nome = nome
        self._dataNascimento = dataNascimento

    def set_rg(self, novo_rg):
        self._rg = novo_rg

    def set_cpf(self, novo_cpf):
        self._cpf = novo_cpf

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_dataNascimento(self, nova_data):
        self._dataNascimento = nova_data

    def get_rg(self):
        return self._rg

    def get_cpf(self):
        return self._cpf

    def get_nome(self):
        return self._nome

    def get_dataNascimento(self):
        return self._dataNascimento

class Conta:

    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self._agencia = agencia
        self._usuario = usuario
        self._dataAbertura = dataAbertura
        self._saldo = saldo

    def get_agencia(self):
        return self._agencia

    def get_usuario(self):
        return self._usuario 

    def get_dataAbertura(self):
        return self._dataAbertura

    def get_saldo(self):
        return self._saldo


print("--- Simulando a Criação de Usuário e Conta ---")

usuario_novo = Usuario()
print(f"1. Usuário concluido com valores aceitaveis: Nome = {usuario_novo.get_nome()}")

print("2. Por favor, digite os dados do novo usuário:")

rg_digitado = int(input("  RG (apenas números): "))
cpf_digitado = int(input("  CPF (apenas números): "))
nome_digitado = input("  Nome completo: ")
data_nascimento_digitada = input(datetime.date(" Data de Nascimento"))


usuario_novo.set_rg(rg_digitado)
usuario_novo.set_cpf(cpf_digitado)
usuario_novo.set_nome(nome_digitado)
usuario_novo.set_dataNascimento(data_nascimento_digitada)

print("3. Dados do usuário atualizados com sucesso.")

agencia_aleatoria = random.randint(0, 999)


