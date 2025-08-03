class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = 0
        self._historico = []
        self.saldo = saldo  # usa o setter

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor

    @property
    def numero(self):
        return self._numero

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self._historico.append(f"Saque de R${valor}")
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo += valor
        self._historico.append(f"Depósito de R${valor}")

    def extrato(self):
        print(f"Cliente: {self._titular} | Saldo Atual: R$ {self._saldo}")
        print("Histórico:")
        for op in self._historico:
            print(" -", op)
