import math
# x=float(input("numero: "))
# print(math.ceil(x))

# x=-3
# print(math.fabs(x))# retorna o valor absoluto de x.

n=3
print(math.factorial(n))#reorna o valor fatorial de um numero

x=3.5
print(math.floor(x)) #retrorna o limite minimo de x, o maior inteiro menor ou igual a x. Se x nao e u ponto flutuante, delega para x. floor cujo qual deve retornar
                    # um valor do tipo integral

y=81
print(math.sqrt(y))# retonra a raiz quadrada de y (math.sqrt(y))

x=2
y=10
print(math.pow(x,y)) # retorna x elevado a potencia de y (math.pow(x,y)

import datetime
print(datetime.date.today())

#formatando datas em strings usando o metodo strftime()
print(datetime.date.today().strftime("%d/%m/%Y")) # com %y = 24 e com %Y = 2024

print(datetime.datetime.now()) # uma vantagem da classe datetime e que ela cnsegue cuidadr da data e do horario ao mesmo tempo
print(datetime.datetime.now().strftime("%d/%m/%Y/%H:%M")) # agora formatando o com a regio do brasil




import time  # Importando o módulo 'time' para usar perf_counter

a = 0
x = time.perf_counter()  # Registra o tempo antes do loop
while a < 10000:
    print(a)
    a += 1
y = time.perf_counter()  # Registra o tempo após o loop
print(y - x)  # Imprime o tempo gasto no loop

#matplot.pyplot as plt # o as fica com apelido do matplot.pyplot usando apenas plt(apelido dado por mim), devem instalar bilbioteca
