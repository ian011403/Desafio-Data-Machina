# Esse é o modulo onde está ficam localizadas as funções que calculam o n-ésimo termo da série de Fibonnaci. 
# Como o método recursivo ocupa mais memória que o método iterativo para numeros muito grandes e também 
# demora mais nessa circunstância, uso o método iterativo na API.

def Fibo_req(n: int) -> int:

    ''' Esta função calcula o n-ésimo termo da sequencia de Fibonnaci usando recursão'''

    # Valores que iniciam a sequência
    if n == 0: return 0
    if n == 1: return 1
    
    # Cálculo recursivo
    F_n = Fibonacci_req(n-1) + Fibonacci_req(n-2)
    
    return F_n

def Fibo(n: int) -> int:

    ''' Esta função calcula o n-ésimo termo da sequência de Fibonacci usando recurssão'''
    
    # Valores que iniciam a sequência
    F_n_1 = 1
    F_n_2 = 0

    if n == 0: return F_n_2
    if n == 1: return F_n_1
    
    # Nessa iteração calculo os últimos dois termos relativos a n
        
    for i in range(n-2):

        F_n_1_novo = F_n_1 + F_n_2 
        F_n_2_novo = F_n_1

        F_n_1 = F_n_1_novo
        F_n_2 = F_n_2_novo
    
    # Finalmente calculo o n-ésimo termo da sequência
    F_n = F_n_1 + F_n_2

    return F_n





