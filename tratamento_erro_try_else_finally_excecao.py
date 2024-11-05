try:
    a=int(input("digite um numero: "))
except:
    print("digite apenas numeros") #o bloco try contera erro caso seja digitada uma letra, e o except trara um açao caso ocorra erro

try:
    a=int(input("digite um numero: "))
except ValueError:
    print("digite apenas numeros") 
except:
    print("erro desconhecido")
finally:
    print("final do algoritmo")