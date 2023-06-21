
class Conta:
    def __init__(self):
        self.agencia = "0001"   
        self.conta = 0
        self.lista_clientes=[]

class Cliente(Conta):
    
    def __init__ (self,nome,endereco,conta):
        super().__init__()
        self.nome= nome
        self.endereco = endereco

    def criar_conta(self):
        self.conta += 1
        self.nome= input("Digite seu nome completo: \n")
        self.endereco= input("Digite seu endereço completo: \n")
        self.lista_clientes.append({'Nome':self.nome,'Endereco':self.endereco,'conta':self.conta,'agencia':self.agencia})
        print("conta criada com sucesso!")

    def exibir_lista_contas(self):
        print(*self.lista_clientes, sep = "\n")
    

#    def __str__ (self):
#        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"
while True:
    opcao_selecionada= int(input("opcao:\n"))
    if opcao_selecionada == 1:
        cliente = Cliente("","","")
        cliente.criar_conta()
        print(f'{cliente.nome},{cliente.endereco},{cliente.conta}')
    elif opcao_selecionada == 2:
        cliente = Cliente("","","")
        cliente.exibir_lista_contas()
    else:
        break