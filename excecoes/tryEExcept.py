# Try, except, else, finally
# a= 18
# b=0
# try:
#     c = a/b
# except ZeroDivisionError as error:
#     print(error)

# print('CONTINUAR')

try:
    print(1)
    8/0
except ZeroDivisionError as e:
    print('Divisão por zero não é permitida')
else:
    print('Executa quando não ocorre erro')
finally:
    print('Executando o finally')
