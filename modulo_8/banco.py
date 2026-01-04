class ContaBancaria:

    # Construtor: que é executado automaticamente quando eu ativar uma nova instancia
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor_deposito):
        self.saldo = self.saldo + valor_deposito
        print(f"Deposito de R$: {valor_deposito} realizado com sucesso!")
    
    def consultarSaldo(self):
        print(f"Saldo atual de: {self.titular}: R$: {self.saldo}")

class ContaCorrente(ContaBancaria):

    def saque(self, valor_saque):
        taxa = 2
        total = valor_saque + taxa

        if (total > self.saldo):
            print("Saldo insuficiente para saque!")
        else:
            self.saldo = self.saldo - total
            print(f"Saque de R$ {valor_saque} realizado com sucesso!")
            print(f"Uma taxa de R4 {taxa} foi aplicada a esta transação.")

class ContaPoupanca(ContaBancaria):

    def saque(self, valor_saque):
        if (valor_saque > self.saldo):
            print("Saldo insuficiente para saque!")
        else:
            self.saldo = self.saldo - valor_saque
            print(f"Saque de R$ {valor_saque} realizado com sucesso!")

sthefany = ContaCorrente('Sthefany', 1000)
aisla = ContaCorrente('Aisla', 2000)
veronica = ContaPoupanca('Verônica', 1000)

print(f"\nDados do 1º Correntista (Conta Corrente) - Nome titular: {sthefany.titular}, Saldo: {sthefany.saldo}")
sthefany.consultarSaldo()
sthefany.depositar(1000)
sthefany.consultarSaldo()
sthefany.saque(500)
sthefany.consultarSaldo()
print("\n")

print(f"Dados do 2º Correntista (Conta Corrente) - Nome titular: {aisla.titular}, Saldo: {aisla.saldo}")
aisla.consultarSaldo()
aisla.depositar(50)
aisla.consultarSaldo()
aisla.saque(2050)
aisla.consultarSaldo()
print("\n")

print(f"Dados do 3º Correntista (Conta Poupança) - Nome titular: {veronica.titular}, Saldo: {veronica.saldo}")
veronica.consultarSaldo()
veronica.depositar(1000)
veronica.consultarSaldo()
veronica.saque(500)
veronica.consultarSaldo()
print("\n")
