# API para identificar veículos ideais para entragas de duas plataformas

## Descrição
No problema dos Veículos Ideais é pedido que se desenvolva uma API que seja capaz de receber um conjunto de itens de uma futura entrega para decidir
quais seriam os veículos ideais para a entrega desses itens para cada uma das plataformas que prestão o serviço. Esses veiculos ideais são os que podem
comportar os itens no menor espaço possível e suportar seus pesos. No caso desse problema, são duas plataformas, a Lala e a Ogi. 

## Conteúdo
### API_vec_ide.py
Esse script cria um servidor local onde fica a API que resolve o problema do veículo ideal. O itens da entrega são enviados em um *request* POST com corpo em formatação JSON, de forma genérica:

[
    { "item": "café", "largura":35, "altura":20, "espessura": 30, "peso":1 },
    { "item": "leite", "largura":35, "altura":20, "espessura": 30, "peso":1 }
]

Para o final /veiculoideal do URL do servidor local criado. O URL do servidor pode ser encontrado ao executar o script da API no terminal.

Após processar os dados o algoritmo pode ou não encontrar um veiculo apropriado, retornando ao usuário uma mensagem em formato JSON, por exemplo:

{ 'Lala': 'Fiorino', 'Ogi': 'Não há veiculo adequado' }








