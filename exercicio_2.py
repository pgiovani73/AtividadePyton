lista=[]
cont=0
lista2=[]
while True:
    n=int(input("insira um valor:"))
    lista.append(n)
    cont=cont+1
    if n==0:
        break
cont=cont-1


media=sum(lista)/cont

while len(lista)>0:
    n=lista[0]-media
    lista2.append(n)

dp=sum(lista2)**(1/2)
print(dp)