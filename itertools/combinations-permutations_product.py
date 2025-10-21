# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia,'
]
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M' , 'G'],
    ['Masculina', 'Feminina', 'Unissex'],
    ['Algodão', 'Poliéster']
]

# combinações de 2 pessoas
print_iter((combinations(pessoas, 2)))

# permutações de 2 pessoas
print_iter((permutations(pessoas, 2)))

# produto cartesiano - todas as combinações possíveis entre os iteráveis
print_iter((product(*camisetas)))
print_iter((product(pessoas, repeat=2)))
