# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def executar_perguntas(perguntas):
    total_acertos = 0

    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        for i, opcao in enumerate(pergunta['Opções']):
            print(f"{i}: {opcao}")
        resposta_usuario = input("Escolha a opção correta (número): ")
        resposta_correta = pergunta['Resposta']

        if pergunta['Opções'][int(resposta_usuario)] == resposta_correta:
            print("Resposta correta!\n")
            total_acertos += 1
        else:
            print(f"Resposta incorreta! A resposta correta é: {resposta_correta}\n")

    print(f"Você acertou {total_acertos} de {len(perguntas)} perguntas.")



executar_perguntas(perguntas)
