# pessoa = {}

# chave = 'nome_completo'

# pessoa[chave] = 'João'
# pessoa['sobrenome'] = "Miranda"

# print(pessoa[chave])

# pessoa[chave] = 'Maria'
# print(pessoa)

# del pessoa['sobrenome']
# print(pessoa)

# # print(pessoa.get('sobrenome'))

# if pessoa.get('sobrenome') is None:
#     print("A chave 'sobrenome' não existe.")
# else:
#     print(pessoa['sobrenome'])

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {'nome': 'Ana',
          'sobrenome': 'Silva',
            'idade': 25
}

# print(len(pessoa))
# print(pessoa.keys())
# print(tuple(pessoa.values()))


# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")

pessoa.setdefault('idade', 30)
