#Nesse modulo defino as classes Veiculo e Iten usadas na resolução 
# do desafio dos veiculos ideais

class Veiculo:

    def __init__(self, largura: float, altura: float, 
                    espessura: float, peso_maximo: float, 
                     veiculo_tipo: str, plataforma: str):
        
        self.larg = largura
        self.alt = altura
        self.esp = espessura
        self.peso_max = peso_maximo
        self.tipo = veiculo_tipo
        self.plat = plataforma
        self.vol = self.larg*self.esp*self.alt

class Item:

    def __init__(self, item,  largura, altura, espessura, peso):
        
        self.larg = largura
        self.alt = altura
        self.esp = espessura
        self.peso = peso
        self.nome = item
        self.vol = self.larg*self.esp*self.alt
                
class Plataforma:

    def __init__(self, nome, lista_veiculos):
        self.nome = nome
        self.veiculos = lista_veiculos
        self.num_vec = len(lista_veiculos)

class Entrega:

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