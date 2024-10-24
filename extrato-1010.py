print("|========= BANCO DO BRASIL =========|\n")
user=int(input("Digite tua Senha: "))
saldo=250
if user==1260:
     print("\n|---------MENU--------|")
     print("|    1 - Extrato      |\n""|    2 - Deposito     |\n""|    3 - Saque        |\n""|    4 - Adm          |\n""|    5 - Sair         |")
     print("|---------------------|")
     op=int(input(" Digite a opção:"))
     if op==1:
         print(" R$",saldo)
     elif op==2:
         deposito=float(input("\n Digite o valor do deposito:R$ "))
         saldo=saldo+deposito
         print(" Valor de Saldo:R$",saldo)
     elif op==3:
         saque=float(input("\n Digite o valor do saque:R$"))
         saldo=saldo-saque
         print(" Valor de Saldo:R$",saldo)
     elif op==4:
        print("\n|---------------------|""\n|  1-Cadastro         |""\n|  2-Editar Cadastro  |""\n|---------------------|\n")
        cadastro=int(input("Escolha a opção:"))
        if cadastro==1:
            print("\nNome: Pedro Giovani Teixeira")
            print("CPF:  582725691-91")
            print("Fone: 67998271385")
            print("sexo: Masculino")
        elif cadastro==2:
            nome=(input("Digite o nome: "))
            cpf=(input("Digite o CPF:"))
            fone=(input("Digite o fone:"))
            sexo=(input("Digite o sexo:"))
            print("\n|---------------------|\n")
            print(" NOME:",nome,"\n CPF:",cpf,"\n FONE:",fone,"\n SEXO:",sexo)
            print("\n|---------------------|")
     elif op==5:
        print("|--------TERMINO DA SESSÃO--------|")
     else:
        print("|----------OPÇÃO INVALIDA---------|")
else:
    print(":( :( ACESO NEGADO :( :(")
