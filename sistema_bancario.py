class Cliente:
    def __init__(self,endereco):
        self.endereco=endereco
        self.contas = []    

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco):
        super().__init__(endereco)
        self.nome= nome
        self.cpf = cpf
        self.agencia= "0001"
        self.numeroconta=0
        self.endereco=endereco


    def criarpessoa(self):
        self.nome = str(input("nome:\n"))
        self.cpf = str(input("cpf:\n"))
        self.numeroconta += 1
        self.contas.append({'nome':self.nome,'cpf':self.cpf,'numeroconta':self.numeroconta,'agencia':self.agencia})
        print(self.contas)

class Conta(Cliente):

    def __init__(self, endereco):
        super().__init__(endereco)
        

    def listar_contas(self):
        print(self.contas)
        
def main():

    while True:
        opcao = int(input('''
        [1]criar cliente
        [2]sair
        [3]listar contas
        '''))
        if opcao == 1:

            cliente = PessoaFisica("","","")
            cliente.criarpessoa()

        elif opcao == 3:
            cliente=Conta()
            cliente.listar_contas

        elif opcao == 2:
            break

main()