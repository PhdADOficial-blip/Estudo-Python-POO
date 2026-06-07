class Poupanca:
    

    def __init__ (self, taxa_renumeracao):
       self.taxa_renumeracao = taxa_renumeracao

    def renumeraConta (self):
        self.saldo += self.saldo * self.taxa_renumeracao