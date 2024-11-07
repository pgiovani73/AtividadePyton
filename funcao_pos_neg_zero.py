def numeros():
    n=int(input("Digite um numero: "))
    if n>0:
        n=("P")
    elif n<0:
        n=("N")
    elif n==0:
        n=("zero")  
    return n

n=numeros()
print (n)
