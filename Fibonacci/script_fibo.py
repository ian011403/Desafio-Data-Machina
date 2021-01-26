# O objetivo dessa scrip é testar a função fibo, do modulo Fibonacci que retorna o n-ésimo 
# termo da sequência de Fibonacci. Esse scrip foi feito para ser usado no terminal para testes rápidos.

from fibo import Fibonacci

n = int(input("Digite qual termo da sequência de Fibonacci você quer calcular:" ))

F_n = Fibonacci(n)

print("O termo " + str(n) + "-ésimo da sequência é " + str(F_n))
