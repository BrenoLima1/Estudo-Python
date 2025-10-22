import json

pessoa = {
    'nome': 'Breno',
    'sobrenome': 'Lima',
    'enderecos': [
        {'rua': 'R1', 'número': 32},
        {'rua': 'R2', 'número': 55},
    ],
    'altura': 1.8,
    'números_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# with open('aula117.json', 'w', encoding = 'utf8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2
#         )

with open('aula117.json', 'r', encoding = 'utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
