from veiculo_ideal import vec_ide

itens = [
    { "item": "café", "largura":35, "altura":20, "espessura": 30, "peso":1 },
    { "item": "leite", "largura":35, "altura":20, "espessura": 30, "peso":1 },
]

resposta = vec_ide(itens)

print(resposta)