"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input("Digite um número inteiro: ")
try:
    inteiro = int(num)
    if inteiro % 2 == 0:
        print(f"O número {inteiro} é par.")
    else:
        print(f"O número {inteiro} é ímpar.")
except ValueError:
    print("Isso não é um número inteiro.")
