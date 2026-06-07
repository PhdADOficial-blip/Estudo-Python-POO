from ClassesHM.conta import Conta
from ClassesHM.Poupanca import Poupanca

class ContaRenumeradaPoupanca(Conta,Poupanca): # a classe crianda chamando duas classes 


    def __init__(self,cliente, numero, saldo, taxa_renumeracao):
        Conta.__init__(self,cliente,numero,saldo)
        Poupanca.__init__(self,taxa_renumeracao)

    def renumeraConta (self):
        self.saldo += self.saldo * (self.taxa_renumeracao / 30)