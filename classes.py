class Documento:

    def __init__(self, numero, data, autor, descricao):
        self.numero = numero
        self.data = data
        self.autor = autor
        self.descricao = descricao

    def impressao(self):
        print('\n', 'Número:', self.numero, '\n', 'Data da criação: ', self.data,
              '\n', 'Autor: ', self.autor, '\n', 'Descrição: ', self.descricao, '\n')


class TipoDocumento(Documento):
    ListaTipo = ['Projeto', 'Propositura', 'DocPerma', 'Oficio']

    ListaProjeto = ['ProjetoDeLei', 'ProjetoDeLeiComplementar',
                    'ProjetosDeResolucao', 'ProjetoDeDecreto', 'PropostaDeEmendaALeiOrganica']
    ListaPropositura = ['Requerimento', 'Indicacao',
                        'MocaoDeAplausos', 'MocaoDePesar', 'MocaoDeRepudio']
    ListaDocPerma = ['Lei', 'LeiComplementar',
                     'Resolucao', 'Decreto', 'EmendaALeiOrganica']
    ListaOficio = ['Presidencia', 'Vereador']

    def __init__(self, tipo):
        self.tipo = self.ListaTipo[tipo]
        print('\n')
        if self.tipo == 'Projeto':
            for indice, valor in enumerate(self.ListaProjeto):
                print(f'Código = {indice}, Tipo do Documento = {valor}')

        elif self.tipo == 'Propositura':
            for indice, valor in enumerate(self.ListaPropositura):
                print(f'Código = {indice}, Tipo do Documento = {valor}')

        elif self.tipo == 'DocPerma':
            for indice, valor in enumerate(self.ListaDocPerma):
                print(f'Código = {indice}, Tipo do Documento = {valor}')

        elif self.tipo == 'Oficio':
            for indice, valor in enumerate(self.ListaOficio):
                print(f'Código = {indice}, Tipo do Documento = {valor}')

        else:
            print("Tipo de documento não especificado")

    def subtype(self, subtipo):

        if self.tipo == 'Projeto':
            self.subtipo = self.ListaProjeto[subtipo]

        elif self.tipo == 'Propositura':
            self.subtipo = self.ListaPropositura[subtipo]

        elif self.tipo == 'DocPerma':
            self.subtipo = self.ListaDocPerma[subtipo]

        elif self.tipo == 'Oficio':
            self.subtipo = self.ListaOficio[subtipo]

        else:
            print("Tipo de documento não especificado")

    def description(self):
        print('O documento é do tipo: ', self.tipo, '/', self.subtipo, '\n')


class User:
    def __init__(self, nome, email, senha):
        self.name = nome
        self.email = email
        self.senha = senha

    def autorizacao(self):
        return f'Muito bem {self.name} seu cadastro esta completo!'
