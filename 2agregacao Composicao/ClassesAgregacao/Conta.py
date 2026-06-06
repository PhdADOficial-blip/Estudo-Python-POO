#Codigo da classe 
class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        

    def depositar(self,valor):
        self.saldo += valor 

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    
    def gerar_extrato(self):
         print(f"Numero: {self.numero}\nSaldo: R${self.saldo}")

    def Trasnfere_Valor (self,Conta_destino,valor):
        if self.saldo < valor:
            return ("saldo Insuficiente")
        else:
            Conta_destino.depositar(valor)
            self.saldo -= valor
            return ("Trasferência Realizada")