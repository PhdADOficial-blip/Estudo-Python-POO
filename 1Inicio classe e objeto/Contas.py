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


#Codigo exemplo 
conta1 = Conta (123,8888888888,"Maria",0)
conta2 = Conta (153,9999999999,"Pedro",20)

#Avaliando se as contas são as mesma para entendermos que na criação do objeto eles são idependentes

if conta1 == conta2:
    print("são iguais")
else:
    print("Sao Diferentes")