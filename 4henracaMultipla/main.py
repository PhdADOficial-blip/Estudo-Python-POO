from Classes.cliente import Cliente
from Classes.conta import Conta
from Classes.superconta import ContaEspecial

cliente1 = Cliente("123","João","Rua X")
cliente2 = Cliente("321","Maria", "Rua Y")
cliente3 = Cliente(456,"Zezinho","Rua Z")

conta1 = Conta(cliente1, 1 , 2000)
conta2 = Conta(cliente2, 2 , 2000)
conta3 = ContaEspecial(cliente3, 3 , 2000, 1000)

conta1.depositar(300)
conta1.Trasnfere_Valor(conta2, 500)

conta2.sacar(700)

conta1.extrato.gerar_extrato(conta1)
conta2.extrato.gerar_extrato(conta2)
conta3.extrato.gerar_extrato(conta3)

conta3.depositar (20000)
conta3.Trasnfere_Valor(conta1,1500)
conta3.extrato.gerar_extrato(conta3)