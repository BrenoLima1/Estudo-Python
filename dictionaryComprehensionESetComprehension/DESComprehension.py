# Dictionary Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# print(produto.items())

dc = {
    chave : valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a','valor a'),
    ('b','valor b'),
    ('c','valor c'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

# Set Comprehension

s1= {2 ** i for i in range(10)}
print(s1)
