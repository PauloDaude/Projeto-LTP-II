class Documento:

    def __init__(self, numero, data, autor, titulo, descricao):
        self.numero = numero
        self.data = data
        self.autor = autor
        self.titulo = titulo
        self.descricao = descricao

    def impressao(self):
        print(f'\nNúmero: {self.numero}\n'
              f'Data da criação: {self.data}\n'
              f'Autor: {self.autor}\n'
              f'Título: {self.titulo}\n'
              f'Descrição: {self.descricao}')


class TipoDocumento(Documento):
    ListaTipo = ['Projeto', 'Propositura', 'Documento Permanente', 'Ofício']

    ListaProjeto = ['Projeto de Lei', 'Projeto de Lei Complementar',
                    'Projetos de Resolução', 'Projeto de Decreto', 'Proposta de Emenda a Lei Orgânica']
    ListaPropositura = ['Requerimento', 'Indicação',
                        'Moção de Aplausos', 'Moção de Pesar', 'Moção De Repúdio']
    ListaDocPerma = ['Lei', 'Lei Complementar',
                     'Resolução', 'Decreto', 'Emenda a Lei Orgânica']
    ListaOficio = ['Presidência', 'Vereador']

    def __init__(self, tipo):
        self.tipo = self.ListaTipo[tipo]
        if self.tipo == 'Projeto':
            print(" Projeto ".center(50, '-').upper())
            for indice, valor in enumerate(self.ListaProjeto):
                print(f"Código [ {indice + 1} ] -> {valor}")

        elif self.tipo == 'Propositura':
            print(" Propositura ".center(50, '-').upper())
            for indice, valor in enumerate(self.ListaPropositura):
                print(f"Código [ {indice + 1} ] -> {valor}")

        elif self.tipo == 'Documento Permanente':
            print(" Documento Permanente ".center(50, '-').upper())
            for indice, valor in enumerate(self.ListaDocPerma):
                print(f"Código [ {indice + 1} ] -> {valor}")

        elif self.tipo == 'Ofício':
            print(" Ofício ".center(50, '-').upper())
            for indice, valor in enumerate(self.ListaOficio):
                print(f"Código [ {indice + 1} ] -> {valor}")

        else:
            print("Tipo de documento não especificado")
        print('-' * 50)

    def subtype(self, subtipo):
        if self.tipo == 'Projeto':
            print(f" {self.ListaProjeto[subtipo]} ".center(50, '-').upper())
            self.subtipo = self.ListaProjeto[subtipo]

        elif self.tipo == 'Propositura':
            print(f" {self.ListaPropositura[subtipo]} ".center(50, '-').upper())
            self.subtipo = self.ListaPropositura[subtipo]

        elif self.tipo == 'Documento Permanente':
            print(f" {self.ListaDocPerma[subtipo]} ".center(50, '-').upper())
            self.subtipo = self.ListaDocPerma[subtipo]

        elif self.tipo == 'Ofício':
            print(f" {self.ListaOficio[subtipo]} ".center(50, '-').upper())
            self.subtipo = self.ListaOficio[subtipo]

        else:
            print("Tipo de documento não especificado")

    def description(self):
        print('Tipo: ', self.tipo, '/', self.subtipo, '\n')


class User:
    def __init__(self, nome, senha):
        self.name = nome
        self.senha = senha

    def autorizacao(self):
        return f'Muito bem {self.name} seu cadastro esta completo!\n'
