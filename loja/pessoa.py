# -*- coding:utf-8 -*-

"""
    Arquivo destinado a classse Pessoa
"""

# inicializaçao da classe
class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome       # Atributos da classe
        self.idade = idade

    
    # Metodo que verifica se a pessoa é adulta
    def is_adult(self):
        return self.idade >= 18


    def __str__(self):
        return f' {self.nome}, Idade {self.idade}'