import unittest
from classes.Cliente import Cliente

class TestCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("João", "11999999999")

    def test_get_nome(self):
        self.assertEqual(self.cliente.nome, "João")

    def test_set_nome(self):
        self.cliente.nome = "Maria"
        self.assertEqual(self.cliente.nome, "Maria")

if __name__ == "__main__":
    unittest.main()
