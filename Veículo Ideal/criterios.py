# Nesse modulo estou definindo os criterios de seleção dos veiculos das plataformas Lala e Ogi com relação ao
# peso total dos itens e peso máximo dos veiculos, volume total de itens e volume máximo dos veiculos além da 
# capacidade de dispor todos os itens dentro de um veículo

# Para encontrar a maneira correta de dispor os itebns de uma entrega no veiculo,
# de maneira a armazenar todos eles, ussei uma bibliotéca que resolve problemas de
# Bin Paking em 3 dimenssões.

# Na biblioteca py3dbp existe uma classe Item, então importei ela com outro nome para não deixar o código confuso. 
# Para simplificar a notação, importei a classe Bin com o nome Container, que seria o espaço de armazenamento de um veículo.

from py3dbp import Packer, Bin
from py3dbp import Bin as Container
from py3dbp import Item as Bloco

from classes_vec_ide import Veiculo, Item, Entrega, Plataforma


def critério_peso_total(plataforma: Plataforma, entrega: Entrega) -> Plataforma:

    """
        Essa função recebe os objetos Plataforma e Entrega, verifica quais veiculos
        possuem peso maximo de transporte inferior ao peso total dos itens da Entrega e retira
        esses veiculos da lista da Plataforma. Após a remoção o objeto Plataforma é retornado 
        pela função.    
    """

    # Antes de verificar o critério é necessário saber se outros critérios não eliminaram os veiculos
    # anteriormente. Se isso ocorreu, basta passar a Plataforma adiante com a lista de veiculos vazia.
    if plataforma.veiculos == []: return plataforma
       
    # Caso contrário, continua a avaliação.
    indice_veiculo = []    

    # Verificam-se quais os veículos que satisfazem o critério de peso total

    for i in range(plataforma.num_vec):
        
        if plataforma.veiculos[i].peso_max >= entrega.peso_total: indice_veiculo.append(i)

    # Em seguida são separados os veiculos que satisfazem 
    nova_lista = []

    for j in indice_veiculo:

        nova_lista.append(plataforma.veiculos[j])
    
    plataforma.veiculos = nova_lista

    # Numero de veiculos é atualizado

    plataforma.num_vec = len(plataforma.veiculos)

    return plataforma

def criterio_volume_total(plataforma: Plataforma, entrega: Entrega) -> Plataforma:

    """
        Essa função recebe os objetos Plataforma e Entrega, verifica quais veiculos
        possuem volume de transporte inferior ao volume total dos itens da Entrega e retira
        esses veiculos da lista da Plataforma. Após a remoção o objeto Plataforma é retornado 
        pela função.    
    """

    # Antes de verificar o criterio é necessário saber se outros critérios não eliminaram os veiculos
    # anteriormente. Se isso ocorreu, basta passar a Plataforma adiante com a lista de veiculos vazia.
    if plataforma.veiculos == []: return plataforma
       
    # Caso contrário, continua a avaliação.

    indice_veiculo = []
    
    # Verificam-se os veículos que satisfazem o critério de volume total

    for i in range(plataforma.num_vec):
        
        if plataforma.veiculos[i].vol >= entrega.vol_total: indice_veiculo.append(i)

    # Em seguida são separados os veiculos que satisfazem 
    nova_lista = []

    for j in indice_veiculo:

        nova_lista.append(plataforma.veiculos[j])
    
    plataforma.veiculos = nova_lista

    # Numero de veiculos é atualizado

    plataforma.num_vec = len(plataforma.veiculos)

    return plataforma

def criterio_disposicao(plataforma: Plataforma, entrega: Entrega) -> Plataforma:

    """
        Essa função verifica se os itens da Entrega podem ser dispostos nos veiculos da Plataforma
        que satisfazem os critérios de peso total, volume total e dimenssões máximas. Essa função 
        resolve esse problema como um Problema de Bin Packing utilizando apenas um bin, que seriam
        os espaços nos veiculos, para buscar descobrir a disposição de itens, dentro dos veiculos, 
        que permite armazenar todos os itens da entrega. Essa solução não considera que os objetos 
        mais pesados estão no 'cão" do veiculo e nem que as orientações dos itens são fixas.
    """

    # Antes de verificar o critério é necessário saber se outros critérios não eliminaram os veiculos
    # anteriormente. Se isso ocorreu, basta passar a Plataforma adiante com a lista de veiculos vazia.
    if plataforma.veiculos == []: return plataforma
       
    # Caso contrário, continua a avaliação do critério de disposição de itens.
    
    # Primeiro, para utilizar a biblioteca de Bin Packing, é instanciado um objeto Packer

    empacotador = Packer()
    
    # Em seguida as dimenssões dos os itens e veículos são adicionados ao 'empacotador' como objetos das classes Bloco e Container
    
    for item in entrega.itens:
        empacotador.add_item( Bloco(name = item.nome, width = item.larg,
                                   height = item.alt, depth = item.esp, weight = 1 ) )

    for veiculo in plataforma.veiculos:
        empacotador.add_bin( Container(name = veiculo.tipo, width = veiculo.larg,
                                        height = veiculo.alt, depth = veiculo.esp, max_weight = entrega.num_itens) )
    
    # Após as configurações iniciais é executado o alguritmo de Bin Packing
    empacotador.pack()

    lista_nome_veiculos_empa = []
    
    # Agora, iterando na lista de Containers é verificado se o numero máxmo de itens armazenados corresponde ao numero de itens da entrega
    for aux in empacotador.bins:
        if len(aux.items) == entrega.num_itens:  lista_nome_veiculos_empa.append(aux.name)
            
    # Em seguida são separados os veiculos que puderam armazenar os itens
    nova_lista = []

    for nome_veic in lista_nome_veiculos_empa:
        for veiculo in plataforma.veiculos:
            if veiculo.tipo == nome_veic: nova_lista.append(veiculo)


    plataforma.veiculos = nova_lista

    # Numero de veiculos é atualizado
    plataforma.num_vec = len(plataforma.veiculos)

    return plataforma

def criterio_capacidade(plataforma: Plataforma) -> Plataforma:

    """ 
        Essa função encontra o veículo de menor capacidade da Plataforma e remove os outros,
        de maneira a sobrar somente o veículo mais barato.
    """
    # Antes de verificar o criterio é necessário saber se outros critérios não eliminaram os veiculos
    # anteriormente. Se isso ocorreu, basta passar a Plataforma adiante com a lista de veiculos vazia.
    if plataforma.veiculos == []: return plataforma
       
    # Caso contrário, continua a avaliação.

    veic_menor_cap = 0

    # Encontra veiculo de menor capacidade
    for i in range(plataforma.num_vec):
        if plataforma.veiculos[i].vol <= plataforma.veiculos[veic_menor_cap].vol: veic_menor_cap = i

    # Remove os de maior capacidade
    plataforma.veiculos = [plataforma.veiculos[veic_menor_cap]]

    # Numero de veiculos é atualizado
    plataforma.num_vec = 1

    return plataforma
