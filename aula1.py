nome = 'Breno Lima'
tamanho_nome = len(nome)
nova_string = ''

for i in nome:
    nova_string += i + '*'
else:
    nova_string = nova_string[:-1]  # Remove o último '*'

print(nova_string)
