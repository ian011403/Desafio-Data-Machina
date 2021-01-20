# Esse é o modulo onde está ficam localizadas as funções que calcula o n-ésimo termo da série de Fibonnaci

def Fibonacci_req(n):

    ''' Esta função calcula o n-ésimo termo da sequencia de Fibonnaci usando recursão'''


    if n == 0: return 0
    if n == 1: return 1

    F_n = Fibonacci_req(n-1) + Fibonacci_req(n-2)
    
    return F_n

def Fibonnaci(n):

    ''' Esta função calcula o n-ésimo termo da sequência de Fibonacci usando recurssão'''

    F_n_1 = 1
    F_n_2 = 0

    if n == 0: return F_n_2
    if n == 1: return F_n_1

    for i in range(n-2):

        F_n_2 = F_n_1
        F_n_1 = F_n_1 + F_n_2 
        
    F_n = F_n_1 + F_n_2

    return F_n





