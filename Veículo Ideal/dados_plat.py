# Nesse módu defino as funções que transferem os dados dos veiculos
# de cada plataforma para a função vec_ide que resolve o problema do
# veiculo ideal.

from classes_vec_ide import Veiculo, Plataforma

def lista_lala() -> Plataforma:

    """ Aqui são instânciados os objetos Veiculo da plataforma Lala. Esses objetos são
        enviados numa lista """

    lala_moto = Veiculo( largura = 35, altura = 40, espessura = 30, 
                        peso_maximo = 20, veiculo_tipo = 'Moto', plataforma = 'Lala' )

    lala_fiorino = Veiculo( 188, 133, 108, 500, 'Fiorino', 'Lala')

    lala_carreto = Veiculo( 300, 180, 200, 1500, 'Carreto', 'Lala')

    lala = Plataforma(nome = 'Lala', lista_veiculos = [lala_moto, lala_fiorino, lala_carreto])

    return lala

def lista_ogi() -> Plataforma:

    """ Aqui são instânciados os objetos Veiculo da plataforma Ogi. Esses objetos são
        enviados numa lista """

    ogi_moto = Veiculo( 52, 36, 52, 20, 'Moto', 'Ogi')

    ogi_suv = Veiculo( 125, 80, 60, 200, 'SUV', 'Ogi')

    ogi = Plataforma('Ogi', [ogi_moto, ogi_suv] )

    return ogi
    
