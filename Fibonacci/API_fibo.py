
# Esse script é reponsavel por criar um servidor e uma API local que retorna o n-ésimo
# termo da sequência de Fibonacci. 
# Aqui escrevo as funcionalidades da API usando o web framework Flask.

# As requests só podem ser feitas usando método POST, com formatação JSON na forma:
#   { 'n': numero }

from flask import Flask, request
from fibo import Fibo

app = Flask("Fibonacci") # Aqui nomeio a aplicação como "Fibonacci"

# Aqui defino a rota para onde será enviado a requesição POST do protocolo HTTP. no final /fibonacci da URL local 
@app.route('/fibonacci', methods= ['POST']) 
def fibonacci():
    #Defino a uma funcionalidade da aplicação

    number = request.get_json() # Converte os dados recebido em fomrato JSON para um dicionário 

    n = number['n'] # Extrai o valor n do termo

    n_termo = Fibo(n) # Calcula o termo n 

    resposta = dict(termo = n_termo) # Cria um dicionário {'termo': n_termo}

    resposta_json = jsonify(resposta) # Cria resposta do servidor no formato JSON

    return resposta_json # Retorna resposta para o usuário

app.run() # Gera o servidor
