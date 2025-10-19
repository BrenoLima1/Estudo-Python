# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
resultado = multiplica(2, 3, 4, 5)
print(f"O resultado da multiplicação é: {resultado}")

# Crie uma função que verifica se um número é par ou ímpar
def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

numero = 10
if verifica_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
