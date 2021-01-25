# Nesse modulo vou definir a função que ira determinar o veiculo ideal para transportar
# um conjunto de itens, para cada plataforma do problema

from classes_vec_ide import Veiculo, Item, Entrega, Plataforma
from dados_plat import lista_lala, lista_ogi
from criterios import criterio_peso_total, criterio_volume_total, criterio_disposicao, criterio_capacidade
from converte import converte_dict_Itens, faz_dicionario

def vec_ide(itens: dict) -> dict:

    """ Essa função recebe um um argumento `itens` que é um dicionário 
        cuja as chaves são os itens e os elementos associados são dicionários
        com as características estruturais do item em questão. Um exemplo seria:

            itens = [
                        { 'item': 'leite', 'larg': 1, 'alt': 2, 'esp': 3, 'pes': 4 },
                        { 'item': 'café', 'larg': 2, 'alt': 50, 'esp': 70, 'pes': 7 }
                    ] 

        Recebendo o dicionário de items essa função consulta os veiculos registrados 
        de cada plataforma, Lala e Ogi, verifica se o volume total de itens, peso total 
        de itens e dimenssões máximas são adequados aos veículos. Se houver mais de um 
        veiculo adequado é selecionado o veículo com menor capacidade. Nesse caso, 
        a função retorna um dicionário cuja a chave é o nome da empresa e o elemento 
        associado é o nome do veiculo:resposta = { 'Lala': 'Fiorino', 'Ogi': 'SUV' }

            resposta = { 'Lala': 'Fiorino', 'Ogi': 'SUV' }

        Caso nenhum veiculo possa transportar os itens, a resposta é: 

            resposta = { 'Lala':'Não há veiculo adequado', 'Ogi':'Não há veiculo adequado' }

        Ou até mesmo: 

            resposta = { 'Lala':'Fiorino', 'Ogi':'Não há veiculo adequado' }
            
    """

    #Primeiro converto o dicionário de itens numa lista de objetos Itens

    lista_itens = converte_dict_Itens(itens)

    #Depois crio o objeto entrega

    entrega = Entrega(lista_itens)        

    # Aqui recebo os dados dos veiculos em forma de listas de objetos Veiculo,
    # uma lista para cada plataforma
    
    lala = lista_lala()
    ogi = lista_ogi()

    # Em seguida são verificados critérios de amarzenamento da entrega para encontrar
    # os dois veiculos ideais

    lala = criterio_peso_total(lala, entrega)
    ogi = criterio_peso_total(ogi, entrega)

    print("--Criterio Peso Total--")
    print("-Lista de veiculos da Lala")
    if lala.veiculos != []:
        for vec in lala.veiculos:
            print(vec.tipo)
    print("-Lista de veiculos da Ogi")
    if ogi.veiculos != []:
        for vec in ogi.veiculos:
            print(vec.tipo)

    lala = criterio_volume_total(lala, entrega)
    ogi = criterio_volume_total(ogi, entrega)

    print("--Criterio Volume Total--")
    print("-Lista de veiculos da Lala")
    if lala.veiculos != []:
        for vec in lala.veiculos:
            print(vec.tipo)
    print("-Lista de veiculos da Ogi")
    if ogi.veiculos != []:
        for vec in ogi.veiculos:
            print(vec.tipo)

    lala = criterio_disposicao(lala, entrega)
    ogi = criterio_disposicao(ogi, entrega)

    print("--Criterio Disposição--")
    print("-Lista de veiculos da Lala")
    if lala.veiculos != []:
        for vec in lala.veiculos:
            print(vec.tipo)
    print("-Lista de veiculos da Ogi")
    if ogi.veiculos != []:
        for vec in ogi.veiculos:
            print(vec.tipo)

    lala = criterio_capacidade(lala)
    ogi = criterio_capacidade(ogi)

    print("--Criterio Capacidade--")
    print("-Lista de veiculos da Lala")
    if lala.veiculos != []:
        for vec in lala.veiculos:
            print(vec.tipo)
    print("-Lista de veiculos da Ogi")
    if ogi.veiculos != []:
        for vec in ogi.veiculos:
            print(vec.tipo)

    # O dicionário com a resposta é criado

    resposta = faz_dicionario(lala, ogi)

    return resposta




        

    



