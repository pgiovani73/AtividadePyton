def calcular_pagamento(qtd_horas,valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas<=40:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
    print(salario)

calcular_pagamento(35,20)#input ja colocado no algoritimo


def calcular_pagamento(qtd_horas,valor_hora):#agora solicitando input
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas<=40:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
    print(salario)
x=input("digite quantidade de horas:")
y=input("digite o valor das horas:")
calcular_pagamento(x,y)
