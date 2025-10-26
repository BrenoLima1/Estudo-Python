from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

    @abstractmethod
    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def detalhes(self):
        print(f'Agência: {self.agencia}, Número: {self.numero}, Saldo: {self.saldo}')

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo=0):
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes()
            return self.saldo

        print('Saldo insuficiente')
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite=0):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= self.limite:
            self.saldo -= valor
            self.detalhes()
            return self.saldo

        print(f'Saldo insuficiente. Seu limite é {self.limite}')
        self.detalhes()

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    print('###')
    cc1 = ContaCorrente(111, 222, 100, 50)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(51)
    print('###')
