# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_sem_nome(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_com_50_anos(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('João', 21)
p2 = Pessoa.criar_com_50_anos(50)      # nome fixo, idade passada
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome("Helena")   # nome passado, idade fixa

print(p1.nome, p1.idade)  # Anônimo 50
print(p2.nome, p2.idade)  # Anônimo 50
print(p3.nome, p3.idade)  # Anônima 23
print(p4.nome, p4.idade)  # Helena 50
