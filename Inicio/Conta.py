#class Conta:  # Criei uma classe onde ainda não implementei nada (não tem atributo nem metodo)
#    pass

class Conta:
    def __init__(self,numero,cpf,nomeTitular,saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular 
        self.saldo = saldo 

c1 = Conta (1, 12345678989, "Pedro", 9000)    #acabei de instanciar (e aqui coloco as cvariaveis atributos da clase )
print(f"nome do titular da conta {c1.nomeTitular}")

