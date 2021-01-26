# Aqui defino algumas funções auxiliares que convertem estruturas de dados do
# desafio do veiculo ideal

from classes_vec_ide import Veiculo, Item, Entrega, Plataforma

def converte_dict_Itens( itens_info: dict ) -> list:

    """ 
        Função que converte lista de dicionários de itens: 
    
        itens_info = [
                    { 'item': 'leite', 'largura': 1, 'altura': 2, 'espessura': 3, 'peso': 4 },
                    { 'item': 'café', 'largura': 2, 'altura': 50, 'espessura': 70, 'peso': 7 }
                ]
    
        Em uma lista de objetos Item.          
    """

    nova_lista = []

    # Os objetos Item são instanciados e armazenados na nova lista

    for item_info in itens_info: 

        item = Item( item_info['item'], item_info['largura'], item_info['altura'],
        item_info['espessura'], item_info['peso'] )

        nova_lista.append(item)

    return nova_lista

def faz_dicionario( lala: Plataforma, ogi: Plataforma ) -> dict: 
    
    ''' 
        Essa função é responsável por criar as respostas que serão retornadas pela função vec_ide(), 
        que serão transformadas em resposta da API para o usuário
    '''
    # Mensages caso os critérios de seleção dos veiculos falhem
    if lala.num_vec > 1: return {'Erro': 'Não selecionou veiculo da Lala'}
    
    if ogi.num_vec  > 1: return {'Erro': 'Não selecionou veiculo da Ogi'}
    
    #Mensagens caso o problema tenha tido uma solução    
    if lala.num_vec == 0 and ogi.num_vec == 1: 
        return { 'Lala':'Não há veiculo adequado', 'Ogi':ogi.veiculos[0].tipo }
    
    if lala.num_vec == 1 and ogi.num_vec == 0: 
        return { 'Lala':lala.veiculos[0].tipo, 'Ogi':'Não há veiculo adequado' }

    if lala.num_vec == 0 and ogi.num_vec == 0: 
        return { 'Lala':'Não há veiculo adequado', 'Ogi':'Não há veiculo adequado' }

    if lala.num_vec == 1 and ogi.num_vec == 1: 
        return { 'Lala':lala.veiculos[0].tipo, 'Ogi':ogi.veiculos[0].tipo }
    
