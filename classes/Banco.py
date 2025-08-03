class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente._nome} adicionado com sucesso!")

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta número {conta.numero} adicionada com sucesso!")

    def buscar_conta_por_numero(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        print("Conta não encontrada.")
        return None

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.buscar_conta_por_numero(numero_origem)
        conta_destino = self.buscar_conta_por_numero(numero_destino)

        if conta_origem is None or conta_destino is None:
            print("Operação de transferência abortada.")
            return

        if conta_origem.saldo < valor:
            print("Saldo insuficiente para transferência.")
            return

        conta_origem.saque(valor)
        conta_destino.deposita(valor)
        print(f"Transferência de R${valor} realizada de conta {numero_origem} para conta {numero_destino}.")