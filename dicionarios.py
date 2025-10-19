pessoa = {}

chave = 'nome_completo'

pessoa[chave] = 'João'
pessoa['sobrenome'] = "Miranda"

print(pessoa[chave])

pessoa[chave] = 'Maria'
print(pessoa)

del pessoa['sobrenome']
print(pessoa)

# print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print("A chave 'sobrenome' não existe.")
else:
    print(pessoa['sobrenome'])
