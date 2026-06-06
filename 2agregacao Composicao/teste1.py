from ClassesAgregacao.Cliente import Cliente
from ClassesAgregacao.Conta import Conta

#testando o Código
cliente1 = Cliente ("123","joao","rua x")
cliente2 = Cliente ("123","Maria","Rua Y")

#Objeto da classe conta -
conta1 = Conta([cliente1,cliente2],111,0)

conta1.gerar_extrato ()
conta1.depositar (1000)
conta1.gerar_extrato ()
conta1.sacar (2000)
conta1.gerar_extrato ()


#Desafio = criar ,mais uma conta para dopis clientes diferenmtes 
#tente imprimir o nome e os endereços dos associados 

