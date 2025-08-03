import unittest
from classes.Banco import Banco
from classes.Cliente import Cliente
from classes.Conta import Conta

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        self.cliente1 = Cliente("João", "11999999999")
        self.cliente2 = Cliente("Maria", "11988888888")
        self.conta1 = Conta(self.cliente1.nome, 1, 100)  # usa propriedade nome
        self.conta2 = Conta(self.cliente2.nome, 2, 50)
        self.banco.adicionar_cliente(self.cliente1)
        self.banco.adicionar_cliente(self.cliente2)
        self.banco.adicionar_conta(self.conta1)
        self.banco.adicionar_conta(self.conta2)

    def test_buscar_conta_por_numero(self):
        conta = self.banco.buscar_conta_por_numero(1)
        self.assertEqual(conta, self.conta1)

    def test_transferir_sucesso(self):
        self.banco.transferir(1, 2, 50)
        self.assertEqual(self.conta1.saldo, 50)
        self.assertEqual(self.conta2.saldo, 100)

    def test_transferir_saldo_insuficiente(self):
        self.banco.transferir(2, 1, 100)  # saldo 50 < 100
        self.assertEqual(self.conta1.saldo, 100)
        self.assertEqual(self.conta2.saldo, 50)

if __name__ == "__main__":
    unittest.main()
