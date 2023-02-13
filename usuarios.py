import os
import json
import atexit
import time

# Armazenar informações de usuário em um dicionário
usuarios = {}


def cadastrar_usuario():
    print(" Cadastro de Usuário ".center(50, '-'))
    nome = input("Usuário: ")
    senha = input("Senha: ")
    usuarios[nome] = senha
    salvar_usuarios()
    print("-" * 50)
    print("Cadastro concluído".center(50))
    print("-" * 50 + "\n")
    login()


def logar_usuario():
    print(" Entrar na conta ".center(50, '-'))
    nome = input("Usuário: ")
    senha = input("Senha: ")
    if nome in usuarios and usuarios[nome] == senha:
        print("-" * 50)
        print(f"Bem-vindo, {nome}!".center(50))
        print("-" * 50 + "\n")

    else:
        print("-" * 50)
        print("Usuário ou senha inválidos".center(50))
        print("-" * 50 + "\n")
        login()


# Carregar usuários do arquivo (se existir)
if os.path.exists("usuarios.json"):
    with open("usuarios.json") as f:
        usuarios = json.load(f)


# Salvar usuários no arquivo ao sair
def salvar_usuarios():
    with open("usuarios.json", "w") as arq_json:
        json.dump(usuarios, arq_json)


atexit.register(salvar_usuarios)


def login():
    opcao = ""
    login_entrar = True
    while opcao not in ["0", "1", "2"]:
        print("Código [ 1 ] - Cadastrar usuário\n"
              "Código [ 2 ] - Entrar na conta\n"
              "Código [ 0 ] - Sair\n")
        opcao = input("Escolha uma opção: ")
        print()
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            logar_usuario()
        elif opcao == "0":
            print("-" * 50)
            print("Saindo do programa...".center(50))
            print("-" * 50 + "\n")
            login_entrar = False
            time.sleep(0.8)
        else:
            print("-" * 50)
            print("Opção Inválida!".center(50))
            print("-" * 50 + "\n")
        return login_entrar
