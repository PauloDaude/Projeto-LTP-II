from classes import Documento, TipoDocumento, User

print("----Bem Vindo!----\nNovo por aqui? Crie já sua conta!")

nome = input("Digite seu nome:")
email = input('Digite seu email:')
senha = input("Digite a sua senha:")

usuario = User(nome, email, senha)
print(usuario.autorizacao())

for indice, valor in enumerate(TipoDocumento.ListaTipo):
    print(f'Código = {indice}, Tipo do Documento = {valor}')

print('\n')

a = TipoDocumento(
    int(input('Digite o número correspondente ao tipo de Documento: ')))

print('\n')

a.subtype(int(input('Digite o número do subtipo de Documento: ')))

print('\n')

numero = input("Digite o número do documento: ")
data = input("Digite a data (em dd/mm/aaaa) do documento: ")
autor = input("Digite o nome do autor: ")
descricao = input("Digite o assunto do documento: ")

print('\n')

c = Documento(numero, data, autor, descricao)

a.description()
c.impressao()
print('\n', "Fim")
