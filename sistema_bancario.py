lista_clientes=[]
class Cliente:
    
    def __init__ (self,nome,endereco):
        self.nome= nome
        self.endereco = endereco
        self.conta = 0

    def criar_conta(self):
        self.conta + 1
        self.nome= input("Digite seu nome completo: \n")
        self.endereco= input("Digite seu endereço completo: \n")
        lista_clientes.append({'Nome':self.nome,'Endereco':self.endereco,'conta':self.conta})
        print("conta criada com sucesso!")

#    def __str__ (self):
#        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"
while True:
    opcao= int(input("opcao:\n"))
    if opcao == 1:
        cliente = Cliente("","")
        cliente.criar_conta()
        print(f'{cliente.nome},{cliente.endereco},{cliente.conta}')
        print(*lista_clientes, sep = "\n")
        
    else:
        break