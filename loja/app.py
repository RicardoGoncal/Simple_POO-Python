# -*- coding:utf-8 -*- 

"""
    Lugar onde a aplicação irá rodar
"""
from datetime import datetime
from cliente import Cliente
from vendedor import Vendedor
from compra import Compras


def main():

    cliente = Cliente('Nome do Cliente', 17)  # Inicia uma instancia da classe Cliente
    vend = Vendedor('Nome do Vendedor', 35, 1500)  # Inicia uma instancia da classe Vendedor

    # Verifica se cliente é maior de idade, se for pode prosseguir com a compra
    if cliente.is_adult():
        
        # Instancia as compras realizadas
        compra1 = Compras(vendedor=vend, data=datetime.now(), valor=50)
        compra2 = Compras(vendedor=vend, data=datetime(2019, 7, 25), valor=150)
        compra3 = Compras(vendedor=vend, data=datetime(2018, 10, 12), valor=300)

        # Registra as compras para o cliente
        cliente.registrar_compra(compra1)
        cliente.registrar_compra(compra2)
        cliente.registrar_compra(compra3)

        print(f'Cliente: {cliente}')    # Exibe o nome e idade do cliente
        print(f'Vendedor: {vend}')      # Exibe o nome e idade do vendedor 

        total_compras = cliente.total_compras()   # Metodo nos traz o valor total da compra
        n_itens = cliente.get_itens()             # Metodo retorna o numero de itens comprados
        

        print(f'Total gasto R${total_compras} em {n_itens} item(ns)')    # Exibe as informações acima
        print(f'Data ultima compra: {cliente.get_data_ultima_compra()}') # Exibe a data da ultima compra

    else:
        print(cliente, 'menor de idade')
    

if __name__ == '__main__':
    main()