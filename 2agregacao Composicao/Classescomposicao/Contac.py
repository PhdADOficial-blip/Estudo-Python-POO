#conta-------<>CLiente
#   |
#   |
#   Extrato



import datetime
from Classescomposicao.Extratoc import Extrato


#Codigo da classe 
class Conta:


    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today ()
        self.extrato = Extrato () # Composição sendo feita pelo atributo 


    def depositar(self,valor):
        self.saldo += valor 
        self.extrato.transacoes.append(['DEPOSITO', valor, datetime.datetime.today()]) #

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SACAR', valor, datetime.datetime.today()])
            return True
    
    def gerar_extrato(self):
         print(f"Numero: {self.numero}\nSaldo: R${self.saldo:10.2f}")

    def Trasnfere_Valor (self,Conta_destino,valor):
        if self.saldo < valor:
            return ("saldo Insuficiente")
        else:
            Conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['TRASFERENCIA',valor, datetime.datetime.today()])
            return ("Trasferência Realizada")