class Banco:
    def __init__(self):
        pass

def criarConta(self,nome,idade,cpf,telefone, senha, saldo):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
    self.tel = telefone
    self.senha = senha
    self.saldo = saldo
    self.cliente = {}
    self.cliente[self.senha]= [self.nome, self.idade, self.cpf, self.tel, self.saldo]
   
def login(self,chave,valor):
    for chave,valor in self.cliente.items():
        if chave == self.senha:
            if valor == self.nome:
                print("Bem vindo")
            else:
                print("Inválido")
        else:
            print("Inválido")

        
def sacar(self, quantia):
    if self.saldo >= quantia:
        self.saldo=- quantia
        print(f"Valor sacado com sucesso! R${quantia}")
    else:
        print("Saldo insuficiente")

def depositar(self,valor):
    self.saldo=+ valor
    print(f"Dinheiro depositado com sucesso! R${self.saldo}")

def transferir(self,valor):
    if self.saldo >= valor:
        self.saldo=- valor
    else:
        print(f"Valor transferido R${valor}")

    
def saldo(self):
    print(f"Seu saldo atual é  R$ {self.saldo}")



