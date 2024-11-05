while True:

    menu =int(input("Escolha a opção\n 1 - soma\n 2 - subtração\n 3 - multiplicação\n 4 - divisão\n 0 - Sair\n"))
    if menu==1:
        soma=float(input("Digite um numero:"))
        soma1=float(input("Digite outro numero:"))
        soma_total=soma+soma1
        print("Resultado da soma:", soma_total,"\n")
    elif menu==2:
        sub=float(input("Digite um numero:"))
        sub1=float(input("Digite outro numero:"))
        sub_total=sub-sub1
        print("Resultado da subtração:", sub_total,"\n")
    elif menu==3:
        mult=float(input("Digite um numero:"))
        mult1=float(input("Digite outro numero:"))
        mult_total=mult*mult1
        print("Resultado da multiplicação:", mult_total,"\n")
    elif menu==4:
        div=float(input("Digite um numero:"))
        div1=float(input("Digite outro numero:"))
        div_total=div+div1
        print("Resultado da divisão:", div_total,"\n")
    elif menu==0:
        print("$$$$-FINALIZANDO-$$$$")
        break
    
    else:
        print("\n%___OPÇÃO INVALIDA__%\n")
