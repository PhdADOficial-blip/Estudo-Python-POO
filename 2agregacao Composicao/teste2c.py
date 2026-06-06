from Classescomposicao.Clientec import Cliente
from Classescomposicao.Contac import Conta

#testando o Código
cliente1 = Cliente ("123","joao","rua x")
cliente2 = Cliente ("123","Maria","Rua Y")

#Objeto da classe conta -
conta1 = Conta([cliente1,cliente2],111,0)


conta1.depositar (1000)
conta1.sacar(300)
conta1.sacar(150)
conta1.depositar (2000)
conta1.sacar(1000)

conta1.extrato.gerar_extrato(conta1.numero)
conta1.gerar_extrato ()
#Desafio = criar ,mais uma conta para dopis clientes diferenmtes 
#tente imprimir o nome e os endereços dos associados 

#CADASTRE MNASI CLIENTES FAÇA SAQUE E TRANFERENCIA DE UMA CONTA PARA PUTRA 
#CRIAR UMA SUPER CLASSES CHAMADA BANCO ARMAZENAR TODOS OS CLIENTES NA CLASSE BANCO 