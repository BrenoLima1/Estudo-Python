# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        # return self.ano_atual - self.idade
        return Pessoa.ano_atual - self.idade #Mais adequado

p1 = Pessoa('Breno', 27)
p1.__dict__['outra'] = 'coisa'
# del p1.__dict__['nome']
# print(p1.__dict__)
print(vars(p1))
print(p1.nome)
