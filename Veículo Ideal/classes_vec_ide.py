# Nesse modulo defino as classes Veiculo, Iten,  Plataforma, e Entrega usadas na resolução 
# do desafio dos veiculos ideais. O objetivo dessas classes não é implementar necessariamente
# um algoritmo baseado em programação orientada a objeto formal, mas apenas organizar os principais 
# elementos do problema

class Veiculo:
    
    ''' Essa classe Veiculo armazena as informações dos veículos das plataformas em uma única estrutura de dados '''
       
    def __init__(self, largura: float, altura: float, 
                    espessura: float, peso_maximo: float, 
                     veiculo_tipo: str, plataforma: str):
        
        self.larg = largura
        self.alt = altura
        self.esp = espessura
        self.peso_max = peso_maximo
        self.tipo = veiculo_tipo
        self.plat = plataforma
        self.vol = self.larg*self.esp*self.alt # Volume do compartimento do veículo

class Item:
    
    ''' Essa classe Veiculo armazena as informações dos veículos das plataformas em uma única estrutura de dados '''
    
    def __init__(self, item,  largura, altura, espessura, peso):
        
        self.larg = largura
        self.alt = altura
        self.esp = espessura
        self.peso = peso
        self.nome = item
        self.vol = self.larg*self.esp*self.alt #volume
                
class Plataforma:

    ''' 
        Essa classe representa a 'entidade' Plataforma, armazenando uma lista de veículos e o numero total de veículos.
        Essa lista de veículos será alterada durante a resolução do problema do Veículo Ideal de maneira a eliminar os
        veículos que não poderiam realizar a entrega dos itens dados.
    '''
    
    def __init__(self, nome, lista_veiculos):
        self.nome = nome
        self.veiculos = lista_veiculos
        self.num_vec = len(lista_veiculos)
        

class Entrega:
    
    ''' Essa classe representa a 'entidade' Entrega, armazenando uma lista de itens dados, numero total de itens, volume total e peso total. '''

    def __init__(self, lista_itens):
        self.itens = lista_itens
        self.num_itens = len(lista_itens)


        peso_total = 0

        for item in lista_itens:

            peso_total += item.peso

        self.peso_total = peso_total


        vol_total = 0

        for item in lista_itens:

            vol_total += item.vol

        self.vol_total = vol_total
