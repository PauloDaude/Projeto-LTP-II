from time import sleep
from classes import Documento, TipoDocumento
import usuarios

print(f"{' Bem Vindo '.center(50, '-')}\nNovo por aqui? Crie já sua conta!")

# --------------------- LOGIN -----------------------------
if usuarios.login():
    sleep(1)

    # -------------- CRIAÇÃO DO DOCUMENTO ---------------------
    print(" Tipo de Documento ".center(50, '-').upper())
    for indice, valor in enumerate(TipoDocumento.ListaTipo):
        print(f"Código [ {indice + 1} ] -> {valor}")
    print('-' * 50)

    print('\n' + '-' * 50)
    tipo = int(input('Digite o código correspondente ao tipo de Documento: '))
    print('-' * 50 + '\n')
    a = TipoDocumento(tipo - 1)

    print('\n' + '-' * 50)
    subtipo = int(input('Digite o código do subtipo de Documento: '))
    print('-' * 50 + '\n')
    a.subtype(subtipo - 1)

    numero = input("Digite o NÚMERO do documento: ")
    data = input("Digite a DATA do documento [dd/mm/aaaa]: ")
    autor = input("Digite o NOME do autor: ")
    titulo = input("Digite o TÍTULO do documento: ")
    descricao = input("Digite a DESCRIÇÃO do documento: ")
    print('-' * 50 + '\n')

    c = Documento(numero, data, autor, titulo, descricao)

    # ------------------- RESULTADO ------------------------
    print(' Documento final '.upper().center(50, '-'))
    a.description()
    c.impressao()
    print('-' * 50)
