# Esse script é reponsavel por criar um servidor com uma API local. 
# A API gerada por esse script resolve o problema do veiculo ideal

from flask import Flask, request, jsonify
from veiculo_ideal import vec_ide

app = Flask("Acha Veículo")

@app.route('/veiculoideal', methods=['POST'])
def veiculo_ideal():

    itens = request.get_json() # Converte os dados recebido em fomrato JSON para um dicionário 

    resposta = vec_ide(itens) # Devolve um dicionário na forma { 'Lala': 'Veiculo', Ogi: 'Veiculo' }

    resposta_json  = jsonify(resposta) # Gera resposta em forma JSON

    return resposta_json  # Retorna resposta para o usuário

app.run()
