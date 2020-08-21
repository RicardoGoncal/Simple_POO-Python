# -*- coding:utf-8 -*-

"""
    Arquivo que contém a classe cliente
    Utilização do conceito de superclasse
"""

from pessoa import Pessoa

# Funcao para coletar somente a data da classe Compras
def get_data(compra):
    return compra.data


# Classe principal (Construtor)
class Cliente(Pessoa):
    """
        Utilização do conceito de Super em Python
    """
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.lista_compras = []
        self.itens = 0

    
    # Metodo que registra uma compra do cliente
    def registrar_compra(self, compra):
        self.lista_compras.append(compra)
        self.itens += 1

    # Metodo que retorna o numero de itens comprados
    def get_itens(self):
        return self.itens


    # Metodo que retorna a ultima data de compra
    def get_data_ultima_compra(self):
        return None if not self.lista_compras else \
            sorted(self.lista_compras, key=get_data)[-1].data


    # Metodo que retorna o valor total da lista de compras
    def total_compras(self):
        if self.lista_compras:
            soma = 0
            for x in self.lista_compras:
                soma = soma + x.valor
            return soma
        else:
            return 'Sem compras para processar o valot total.'
