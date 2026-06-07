class Conta:
    
    __total_contas = 0 # Criando um atributos de classe onde deixamos privados 
    
    @classmethod   # decorador para metodo de classes 
    def get_total_contas(cls):
        return cls.__total_contas
    
    
    @staticmethod  #Metodos estatico pode ser chamado sem ter um valor, chamadno direto da classe
    def nome_banco ():
        return "Banco Pedro"



    def __init__ (self,numero, saldo):
        self.__numero = numero # ao colocar __ eun deixo os atributos encapsulado
        self.__saldo = saldo 
        type(self).__total_contas += 1 # Contador atribuidor de contador de classes ele contan ao instaciar um novo objeto 

    
    @property # decorador par aprintar os valores dos atributos de objetos 
    def saldo(self):
        return self.__saldo

    @saldo.setter # decorador para manipular os atributos de classes encapsuladas 
    def saldo(self,valor):
        if valor < 0 :
           print("saldo invalido")
        else:
         self.__saldo = valor        
   

    def sacar (self,valor): # __ posso tambem encapsular as funções 
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            return True
    
    def gerar_saldo(self):
        print(f"conta: {self.__numero}")
        print(f"Saldo: R${self.__saldo:10.2f}")

        