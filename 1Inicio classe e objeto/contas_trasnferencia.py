#Codigo da classe 
class Conta:
    def __init__(self,numero,cpf,nomeTitular,saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular 
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
         print(f"Numero: {self.numero}\nCPF: {self.cpf}\nNome: {self.nomeTitular}\nSaldo: R${self.saldo}")

    def TrasnfereValor (self,Contadestino,valor):
        if self.saldo < valor:
            return ("saldo Insuficiente")
        else:
            Contadestino.depositar(valor)
            self.saldo -= valor
            return ("Trasferência Realizada")



#Codigo exemplo 
conta1 = Conta (123,8888888888,"Maria",100)
conta2 = Conta (153,9999999999,"Pedro",100)

print(conta1.TrasnfereValor(conta2,50))

conta1.gerar_extrato ()

conta2.gerar_extrato ()