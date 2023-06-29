from datetime import datetime
from abc import ABC, abstractclassmethod, abstractproperty
import textwrap

class Cliente:
    def __init__(self,endereco):
        self.endereco=endereco
        self.contas = []  

    def realizartransacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionarconta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, nome, cpf, endereco,datanascimento):
        super().__init__(endereco)
        self.nome= nome
        self.cpf = cpf
        self.datanascimento= datanascimento
        

class Conta():

    def __init__(self,cliente,numero):
        self._saldo =0
        self._cliente = cliente
        self._numero= numero
        self._agencia= "0001"
        self._historico =Historico()

    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self.saldo
        excedeulimite = valor > saldo

        if excedeulimite:
            print("nao é possivel realizar o saque. Valor acima do disponivel!")

        elif valor < 0:
            print("Adicione um valor maior que 0!")

        elif valor > 0: 
            self._saldo -= valor
            print("operação realizada!")
            return True

        else:
            print("operação falhou!")

        return False
    
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print("operação realizada!")
            
        else:
            print("operação falhou!")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite = 500, limite_saques = 3):
        super().__init__(cliente, numero)
        self.limite= limite
        self.limite_saques = limite_saques

    def sacar(self,valor):

        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):

        self.trasacoes.append({'Tipo': transacao.__classe__.__name__,
                               'Valor':transacao.valor,
                               'Data':datetime.now().strftime("%d-%m-%Y %H:%M:%s")
                               })
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def Depositar(clientes):
    cpf = str(input("DIGITE SEU cpf:\n"))
    cliente = filtrar_cliente(cliente,cpf)

    if not cliente:
        print("Cliente nao encontrado!")
        return
    valor = float(input("Insira o valor a ser depositado:\n"))
    Transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
         return

    cliente.realizar_transacao(conta, Transacao)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def Sacar(clientes):
    cpf = str(input("DIGITE SEU cpf:\n"))
    cliente = filtrar_cliente(cliente,cpf)

    if not cliente:
        print("Cliente nao encontrado!")
        return
    
    valor = float(input("Insira o valor a ser depositado:\n"))
    Transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
         return

    cliente.realizar_transacao(conta, Transacao)

def main():
    clientes = []
    contas =[]

    while True:
        opcao = menu()
        if opcao == 1:
            Depositar(clientes)

        elif opcao == 2:
            Sacar(clientes)

        
            

        elif opcao == 2:
            break

main()