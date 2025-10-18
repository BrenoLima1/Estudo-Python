"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
tamanho_palavra = len(palavra_secreta)
nova_string = ''

print('Bem vindo ao jogo de adivinhação!')
print(f'A palavra secreta tem {tamanho_palavra} letras.')

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) != 1:
        print('Por favor, digite apenas uma letra.')
        continue

    tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        print(f'Você acertou a letra: {letra_digitada}')
    else:
        print(f'Você errou! A letra {letra_digitada} não está na palavra.')

    nova_string = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            nova_string += letra
        else:
            nova_string += '*'

    print(f'Palavra até agora: {nova_string}')

    if nova_string == palavra_secreta:
        print(f'Parabéns! Você adivinhou a palavra secreta "{palavra_secreta}" em {tentativas} tentativas.')
        break
