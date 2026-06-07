
from ClassesHM.conta import Conta
from ClassesHM.cliente import Cliente
from ClassesHM.ContaRenumeradaPoupanca import ContaRenumeradaPoupanca
from ClassesHM.Poupanca import Poupanca

Cliente1 = Cliente(123,"Pedro", "rua x")

Conta1 = ContaRenumeradaPoupanca(Cliente1,1,10000,0.5)
Conta2 = Conta(Cliente1,2,10000)

Conta1.renumeraConta()
Conta1.gerar_extrato ()