import contas

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome      # usamos "_" para indicar atributo "protegido"
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

    # Getter para nome
    @property
    def nome(self):
        return self._nome

    # Setter para nome
    @nome.setter
    def nome(self, nome: str):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = nome

    # Getter para idade
    @property
    def idade(self):
        return self._idade

    # Setter para idade
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        self._nome = nome      # usamos "_" para indicar atributo "protegido"
        self._idade = idade
        self.conta: contas.Conta | None = None


if __name__ == "__main__":
    c1 = Cliente('Ana', 20)
    c1.conta = contas.ContaCorrente(111, 222, 0)
    print(c1)
    print(c1.conta)
    print('###')
    c2 = Cliente('Paulo', 22)
    c2.conta = contas.ContaPoupanca(111, 222, 0)
    print(c2)
    print(c2.conta)
