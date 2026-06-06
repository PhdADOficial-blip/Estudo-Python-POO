class Extrato: #aqui criei uma lista  para cria o extrato por composição 


    def __init__ (self):
          self.transacoes = []

    def gerar_extrato(self, conta):
        print(f"Estrato da conta {conta}")
        for tran in self.transacoes:
            print(f"{tran[0]:15s} {tran[1]:10.2f} {tran[2].strftime('%d/%b/%y')}")



#Formatação: [0- Tipo 1 - Valor 2 - Data]