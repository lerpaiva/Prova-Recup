from classes import *
import os
usuario = Banco()
def main():
    sair = False
    while sair == False:
        try:
            print("--Bem vindo ao Banco--")
            print()
            print("O que deseja fazer?")
            print("[1] Criar conta \n[2] Fazer Login \n[3] Sair ")
            menu = int (input("--> "))
            match menu:
                case 1:
                    os.system("cls")
                    print("Preencha as informações abaixo:")
                    nome = input("Nome: ")
                    idad = int(input("Idade: "))
                    cpf = int(input("CPF: "))
                    telefone = int(input("Telefone: "))
                    sen = int(input("Crie uma senha:"))
                    sal = float(input("Informe seu saldo inicial: "))
                    usuario.criarConta(nome,idad,cpf,telefone,sen,sal)
                    os.system("pause")
                case 3:
                    os.system("cls")
                    sair = True 
                    os.system("pause")
                case 2:
                    os.system("cls")
                    print("Preencha para fazer login ")
                    nom = input ("Informe seu nome: ")
                    senh  = int("Informe  sua senha: ")
                    for senh,nom in usuario.login(senh,nom):
                        print("O que deseja fazer: ")
                        print("[1] Sacar")
                        print("[2] Depositar")
                        print("[3] Transferir")
                        print("[4] Checar saldo")
                        print("[5] Sair")
                        men = int(input("--> "))
                        match men:
                            case 1:
                                retirar = float(input("Quanto gostaria de sacar?: "))
                                usuario.sacar(retirar)
                            case 2:
                                dep = float(input("Quanto gostaria de depositar?: "))
                                usuario.depositar(dep)
                            case 3:
                                pessoa = input("Digite o nome do remetente: ")
                                for pessoa in usuario:

                                    transf = float(input("Valor a trasnferir: "))
                                    usuario.transferir(transf)
                                    pessoa.self.saldo=+ transf
                            case 4:
                                usuario.saldo()
                            case 5:
                                sair = True
                            case _:
                                print("opção inválida")
                                os.system("cls")
                    os.system("pause")
                case _:
                    os.system("cls")
                                



            

        except Exception as erro:
            print("Opção inválida")
