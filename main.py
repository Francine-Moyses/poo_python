from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.Banco import Banco
from colorama import init, Fore, Style
import emoji

# Inicializa colorama (Windows precisa disso)
init(autoreset=True)

banco = Banco()

def print_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n🏦 Bem-vindo ao Banco POO Python! 🏦")
    print(Fore.YELLOW + "===============================")
    print(Fore.GREEN + "1️⃣  - Criar Cliente e Conta")
    print("2️⃣  - Depositar")
    print("3️⃣  - Sacar")
    print("4️⃣  - Transferir")
    print("5️⃣  - Extrato")
    print("6️⃣  - Sair")
    print(Fore.YELLOW + "===============================")

while True:
    print_menu()
    opcao = input(Fore.MAGENTA + "Escolha uma opção: " + Style.RESET_ALL)

    if opcao == "1":
        print(Fore.CYAN + emoji.emojize("✨ Criar Cliente e Conta ✨"))
        nome = input("Nome do cliente: ")
        fone = input("Telefone: ")
        cliente = Cliente(nome, fone)
        numero = int(input("Número da conta: "))
        conta = Conta(cliente.nome, numero, 0)
        banco.adicionar_cliente(cliente)
        banco.adicionar_conta(conta)
        print(Fore.GREEN + "✅ Conta criada com sucesso!")

    elif opcao == "2":
        print(Fore.CYAN + emoji.emojize("💰 Depositar 💰"))
        numero = int(input("Número da conta: "))
        valor = float(input("Valor para depósito: "))
        conta = banco.buscar_conta_por_numero(numero)
        if conta:
            conta.deposita(valor)
            print(Fore.GREEN + f"✅ Depósito de R${valor:.2f} realizado!")
        else:
            print(Fore.RED + "❌ Conta não encontrada!")

    elif opcao == "3":
        print(Fore.CYAN + emoji.emojize("🏧 Sacar 🏧"))
        numero = int(input("Número da conta: "))
        valor = float(input("Valor para saque: "))
        conta = banco.buscar_conta_por_numero(numero)
        if conta:
            conta.saque(valor)
        else:
            print(Fore.RED + "❌ Conta não encontrada!")

    elif opcao == "4":
        print(Fore.CYAN + emoji.emojize("🔁 Transferir 🔁"))
        origem = int(input("Conta de origem: "))
        destino = int(input("Conta de destino: "))
        valor = float(input("Valor: "))
        sucesso = banco.transferir(origem, destino, valor)
        if sucesso:
            print(Fore.GREEN + "✅ Transferência realizada com sucesso!")
        else:
            print(Fore.RED + "❌ Falha na transferência!")

    elif opcao == "5":
        print(Fore.CYAN + emoji.emojize("📄 Extrato 📄"))
        numero = int(input("Número da conta: "))
        conta = banco.buscar_conta_por_numero(numero)
        if conta:
            conta.extrato()
        else:
            print(Fore.RED + "❌ Conta não encontrada!")

    elif opcao == "6":
        print(Fore.YELLOW + "👋 Obrigado por usar nosso sistema! Até logo!")
        break

    else:
        print(Fore.RED + "⚠️ Opção inválida. Tente novamente.")
