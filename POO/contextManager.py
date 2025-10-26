# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo, modulo, encoding = 'utf8'):
        self.caminho_arquivo = caminho_arquivo
        self.modulo = modulo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modulo)
        return self._arquivo

    def __exit__(self, class_exception, exceptiom_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

instancia = MyOpen('aula149.txt', 'w')

with instancia as alguma_coisa:
    alguma_coisa.write('Linha 1\n')
    alguma_coisa.write('Linha 2\n')
    alguma_coisa.write('Linha 3\n')
    print('WITH', alguma_coisa)
