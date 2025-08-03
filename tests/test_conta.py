import unittest
from classes.Conta import Conta

class TestConta(unittest.TestCase):
    def setUp(self):
        self.conta = Conta("Maria", 1, 100)

    def test_saque_valido(self):
        self.conta.saque(50)
        self.assertEqual(self.conta.saldo, 50)

    def test_saque_invalido(self):
        self.conta.saque(200)
        self.assertEqual(self.conta.saldo, 100)

    def test_deposito(self):
        self.conta.deposita(50)
        self.assertEqual(self.conta.saldo, 150)

if __name__ == "__main__":
    unittest.main()
