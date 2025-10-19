"""
Faça uma lista de compras com listas. O usuário deve poder inserir, apagar e listar os itens da lista.
Não permita que o programa quebre com erros de índice inválido ou comandos inválidos.
"""

decisao = input("Bem-vindo à lista de compras! Você deseja (i)nserir, (a)pagar ou (l)istar itens? ").lower();
lista_de_compras = []

while decisao in ['i', 'a', 'l']:
    if decisao == 'i':
        item = input("Digite o item que deseja inserir na lista de compras: ")
        lista_de_compras.append(item)
        print(f"'{item}' foi adicionado à lista de compras.")
    elif decisao == 'a':
        try:
            indice = int(input("Digite o índice do item que deseja apagar (começando de 0): "))
            item_removido = lista_de_compras.pop(indice)
            print(f"'{item_removido}' foi removido da lista de compras.")
        except (IndexError, ValueError):
            print("Índice inválido. Por favor, tente novamente.")
    elif decisao == 'l':
        if lista_de_compras:
            print("Itens na sua lista de compras:")
            for i, item in enumerate(lista_de_compras):
                print(f"{i}: {item}")
        else:
            print("Sua lista de compras está vazia.")

    decisao = input("Você deseja (i)nserir, (a)pagar ou (l)istar itens? ").lower()
else:
    print("Comando inválido. Encerrando o programa.")
