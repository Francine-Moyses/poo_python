class Main:
    pass

from classes.Cliente import Cliente

from classes.Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome(),1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()