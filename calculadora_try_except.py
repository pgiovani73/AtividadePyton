try:
    while True:

        menu =int(input("Escolha a opção\n1:soma - 2:subtração - 3:multiplicação - 4:divisão - 0:Sair\n"))
        if menu==1:
            soma=float(input("Digite um numero:"))
            soma1=float(input("Digite outro numero:"))
            soma_total=soma+soma1
            print("Resultado:", soma_total,"\n")
        elif menu==2:
            sub=float(input("Digite um numero:"))
            sub1=float(input("Digite outro numero:"))
            sub_total=sub-sub1
            print("Resultado:", sub_total,"\n")
        elif menu==3:
            mult=float(input("Digite um numero:"))
            mult1=float(input("Digite outro numero:"))
            mult_total=mult*mult1
            print("Resultado:", mult_total,"\n")
        elif menu==4:
            div=float(input("Digite um numero:"))
            div1=float(input("Digite outro numero:"))
            div_total=div+div1
            print("Resultado:", div_total,"\n")

        elif menu==0:
            print("$_$_$_-FINALIZANDO-$_$_$_")
            break
except:
    print("digite apenas numeros:")      