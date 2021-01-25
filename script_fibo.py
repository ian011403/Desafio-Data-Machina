# O objetivo dessa API é receber um numero inteiro n do usuário e
# processar o n-ésimo termo da sequência de Fibonacci chamando a função
# ótima Fibonacci do modulo fibo

# Essa API pode recerber um arquivo .txt com multiplas entradas, retornando 
# para cada entrada o devido termo da sequencia de FIbonacci. A respostas serão
# escritas na mesmo ordem com que aparecem as entradas no arq. txt. 
# 
# A sintaxe desse arquivo deve ser de uma entrada a cada linha, para facilitar a 
# visualização das respsotas posteriormente.   

from fibo import Fibonacci

resposta = input("Deseja usar arquivo com multiplas entradas? (Digite s ou n)")

if resposta == s:

    file = input("Escreva o caminho até o arquivo a partir da root ou do diretorio atual")


if resposta == n

    n = int(input("Digite qual termo da sequência de Fibonacci você quer calcular:" ))

    F_n = Fibonacci(n)

    print("O termo " + str(n) + "-ésimo da sequência é " + str(F_n))