
# Esse script é reponsavel por criar um servidor com uma API local que retorna a n-ésimo
# termo da sequÊncia de Fibonacci. 
# Aqui escrevo as funcionalidades da API usando o web framework Flask.

from flask import Flask, request
from fibo import Fibo

app = Flask("Fibonacci") # Aqui nomeio a aplicação como "Fibonacci"

# Aqui defino a rota para onde será enviado o requesição POST do protocolo HTTP
@app.route('/fibonacci', methods= ['POST']) 
def fibonacci():
    #Defino a aplicação

    number = request.get_json() # Converte o formato JSON para dicionário 

    n = number['n'] # Extra o valor n do termo

    n_termo = Fibo(n) #Calcula o termo 

    resposta = dict(termo = n_termo) # Cria um dicionário {'termo': n_termo}

    resposta_json = jsonify(resposta) # Cria resposta do servidor no formato JSON

    return resposta_json # Retorna resposta para o usuário

app.run() # Gera o servidor