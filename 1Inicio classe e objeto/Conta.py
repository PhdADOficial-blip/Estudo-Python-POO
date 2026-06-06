#class Conta:  # Criei uma classe onde ainda não implementei nada (não tem atributo nem metodo)
#    pass
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
         




#Codigo do Exemplo 
#INSTANCIANDO UM OBJETO 
#NOME DO OBJETO = NOME DA CLASSE (VARIAIVEIS NA ORDEM ATRIBUTOS)
c1 = Conta (1, 12345678989, "Pedro", 9000)    #acabei de INSTACIAR (e aqui coloco as cvariaveis atributos da clase )
#depositar
c1.depositar(500)

#sacar
valor_saque = 5000
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
      print(f"Saque de R${valor_saque} Realizado Com Sucesso!")
else:
      print(f"saldo insuficiente para realizar o saque")




c1.gerar_extrato ()





