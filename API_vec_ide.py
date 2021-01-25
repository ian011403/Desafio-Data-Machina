# Esse script é reponsavel por criar um servidor com uma API local. 
# Aqui escrevo as funcionalidades da API usando o web framework Flask.
# A API gerada por esse script resolve o problema do veiculo ideal

from flask import Flask, request
from veiculo_ideal import vec_ide

app = Flask("Acha Veículo")
app.config["DEBUG"] = True

@app.route('/veiculoideal', methods=['POST'])
def veiculo_ideal():

    itens = request.get_json() 

    resposta = vec_ide(itens)

    resposta_json  = jsonify(resposta)

    return resposta_json  

app.run()