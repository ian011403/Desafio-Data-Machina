# API para calcular n-ésimo termo da seência de Fibonacci

## Descrição
Nesse repositório encontram diversos scripts utilizados para o desenvolvimento da API que calcula o n-ésimo termo da sequência de Fibonacci

## Conteúdo

### API_fibo.py
Essa script é responsável por criar o servidor local com a API que calcula o n-ésimo termo da sequÊncia de Fibonacci. A API é encontrada no final /fibonacci da URL e 
recebe apenas métodos POTS de *request* cujo o corpo é escrito com a sitaxe do JSON, que deve possuir a forma {"n": número}, sendo *número* o termo da sequência que será
calculado pela API.

### fibo.py
Esse é um modulo com duas funções que calculam a sequencia de Fibonacci, uma função recursiva e outra iterativa. A função iterativa é a mais eficas e é a utilizada na API.

### scrip_fibo.py
Essa é uma scrip que recebe no terminal o valor n do n-ésimo termo e retorna esse o valor desse termo via terminal. Esse script foi feito para testes simples.


