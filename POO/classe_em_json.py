# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'classe.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def salvar_json(dados):
    with open(CAMINHO_ARQUIVO, 'w', encoding = 'utf8') as arquivo:
        json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=2
                )

p1 = Pessoa('João', 32)
p2 = Pessoa('Maria', 12)
p3 = Pessoa('Luane', 40)
bd = [vars(p1), p2.__dict__, vars(p3)]
salvar_json(bd)
