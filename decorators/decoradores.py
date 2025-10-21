# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)



def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado =  func(*args, **kwargs)
        print(f'O seu resultado foi: {resultado}')
        print("Decorada")
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(inverte_string.__name__)
    return string[::-1]


def is_string(parame):
    if not isinstance(parame, str):
        raise TypeError("O parâmetro deve ser uma string")

# inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('123')
print(invertida)
