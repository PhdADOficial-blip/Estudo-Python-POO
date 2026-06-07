from Classes.conta import Conta
import datetime

class ContaEspecial(Conta):

    def __init__(self,clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite    # adicionadno somente o atributo diferente ( limite )
    
    def sacar(self,valor): # sobreescrevemos o metodo sacar 
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente conta numero {self.numero} Cliente {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(['SAque', valor, datetime.datetime.today()])
            return True
