from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco,cpf,nome,data_nascimento):
        super().__init__(endereco)
        self._cpf= cpf
        self._nome= nome
        self._data_nascimento= data_nascimento

class Conta:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls,numero,cliente):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self._saldo
        excedeu_limite = valor > saldo

        if excedeu_limite:
            print ("\nlimite excedido! Insira outro valor")    
        elif valor < 0:
            print("\nInsira valor acima de 0")
    
        else:
            self.saldo -= valor
            print("\nOperação de saque realizada com sucesso!")
            return True   
         
        return False
    
    def depositar(self,valor):

        if valor > 0:
            self._saldo += valor
            print("\nOperação de deposito realizada com sucesso!")
            return True
        elif valor < 0:
            print(("\nInsira valor acima de 0"))
        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500,limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self,valor):

        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_limite_saque = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\nSeu saque excedeu o limite de R$ 500,00")

        elif excedeu_limite_saque:
            print("\nSeus saques ja ultrapassam 3 saques disponiveis")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome} 
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
        














