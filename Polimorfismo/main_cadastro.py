from Cadastro import *


while True:


    print("|============ CADASTROS ============|")
    print("\n|-------------MENU----------------|")
    print("|    1 - Dados Pessoa Fisica      |\n""|    2 - Dados Pessoa Juridica    |"|\n     0 - sair         |")
    print("|---------------------------------|")

    dados=int(input(" Digite a opção:"))
    if dados==1:
        print("\nDados Pessoa Fisica")
        dados=Pessoal()
        dados.pf()
        print("Cadastro Realizado")
    elif dados==2:
        print("\nDados Pessoa Juridica ")
        dados=Empresa()
        dados.pj()
        print("Cadastro Realizado")
    elif dados==0:        
        print("saindo")
        break   
        

# x=Empresa()
# x.pj()

# y=Pessoal()
# y.pf()