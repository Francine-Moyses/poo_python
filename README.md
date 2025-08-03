# 🐍 POO em Python – Projeto de Estudos

Este projeto foi criado com o objetivo de praticar os fundamentos de **Programação Orientada a Objetos (POO)** utilizando a linguagem Python. Ele é estruturado de forma simples e didática, com foco em aprendizado e organização de código.

---

## 📁 Estrutura do Projeto
```
.
├── classes/
│   ├── Banco.py              # Classe que gerencia contas e clientes
│   ├── Cliente.py            # Classe Cliente com atributos e métodos
│   ├── Conta.py              # Classe Conta com operações bancárias
│   ├── __init__.py
│   └── __pycache__/          # Arquivos de cache do Python (ignorar no Git)
│
├── tests/                    # Testes automatizados com unittest
│   ├── test_banco.py
│   ├── test_cliente.py
│   ├── test_conta.py
│   ├── __init__.py
│   └── __pycache__/          # Arquivos de cache do Python (ignorar no Git)
│
├── main.py                   # Menu interativo e execução do sistema bancário
├── requirements.txt          # Dependências do projeto (colorama, emoji, etc.)
├── README.md                 # Documentação do projeto
└── .gitignore                # Arquivos e pastas ignoradas pelo Git

```

---

## 🔧 Tecnologias utilizadas

- Python 3.11+
- VS Code
- Git + GitHub

---

## 📚 Conceitos de POO aplicados

- Classes e Objetos
- Construtores (`__init__`)
- Atributos de instância
- Métodos
- Encapsulamento (em breve)
- Herança (em breve)

---

## ▶️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/poo_python_estudos.git
   cd poo_python_estudos
   ```
2. Crie e ative um ambiente virtual (Opcional):
   ```bash
   python -m venv venv
   venv\Scripts\activate   # No Windows
   source venv/bin/activate  # No Linux/macOS
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o projeto:
   ```bash
   python main.py
   ```
---

## 🧪 Executando os testes

Para rodar todos os testes com unittest, use:
   ```bash
   python -m unittest discover -s tests
   ```
---

## 📌 Funcionalidades

- Criar cliente e conta
- Realizar depósito
- Efetuar saque
- Transferência entre contas
- Consultar extrato
- Interface de terminal com emojis e cores (colorama e emoji)

---

## 📝 Licença
Este projeto é livre para fins de estudo e aprendizado. Nenhuma licença específica foi aplicada.
