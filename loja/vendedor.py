# -*- coding:utf-8 -*-

"""
    Arquivo que contém a classe vendedor
    Utilização do conceito de superclasse
"""

from pessoa import Pessoa

# Classe principal (Construtor)
class Vendedor(Pessoa):
    """
        Utilização do conceito de Super em Python
    """
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


    # Metodo que retorna o salario do vendedor
    def get_salario(self):
        return self.salario