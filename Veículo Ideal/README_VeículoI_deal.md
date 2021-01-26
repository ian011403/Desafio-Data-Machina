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

### classes_vec_ide.py
Para tornar a resolução do problemas mais simples foram criadas as classes Item, Veículo, Entrega e Plataforma, declaras no módulo classes_vec_ide. As classes Item e Veiculo armazenam principalmente as itentificações de itens e veiculos além de suas características físicas como volume, dimenssões e pes. Os objetos Item que representão os itens de interesse do problema são armazenados em um objeto Entrega, que guarda a lista de itens e o numero total deles. O mesmo vale para o caso do objeto Plataforma.

### dados_plat.py
Uma vez definidas as classes usadas no problema, pode-se usar as descrições físicas dos veículos para criar objetos *Veículo*. Esse processo ocorre nas funções *lista_lala* e *lista_ogi*, presentes no módulo **dados_plat**. Essas funções, além de instanciar os Vículos, os armazena numa lista que é usada para instanciar uma Plataforma dentro da mesma função, que no final, retorna esse último objeto instanciado. 
Todo esse tipo de procedimento de reunião de dados sobre as plataformas foi localizado em funções específicas com o intuito de facilitar uma possível construção de funções lista_lala e lista_ogi capazes de acessar uma estrutura de dados a parte do módulo.

### veiculo_ideal.py
A função responsável por juntar as informações dos itens e dos veiculos para decidir quais são os veículos ideias para realzar a entrega é a função *vec_ide*, presente no módulo **veiculo_ideal**. Essa função recebe a lista de itens, instância os objetos *Item* e armazena-os numa lista usada para instanciar o objeto *Entrega*. Além disso, essa função também recebe os objetos *Plataforma* gerados pelas funções *lista_lala* e *lista_ogi* do módulo **dados_plat**. Dessa forma, com os dados de itens e veículos, a função *vec_ide* pode começar a executar critérios de eliminção de veículos considerados não ideais.

### criterios.py
Os critérios de eliminação de veículos de cada plataforma são definidos como funções no módulo **criterios**. 






