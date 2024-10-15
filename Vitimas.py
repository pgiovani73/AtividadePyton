print("responda sim ou nao as perguntas abiaxo")
telefone=input("telefonou pra vitima?:")
local=input("Esteve no local do crime?:")
morar=input("Mora perto da vitima?:")
divida=input("Devia a vitima?:")
trabalho=input("trabalhou com a vitima?:")
contador=0
if telefone=="sim":
    contador+=1

if local=="sim":
    contador+=1
if morar=="sim":
    contador+=1
if divida=="sim":
    contador+=1
if trabalho=="sim":
    contador+=1

if contador==5:
    print("Assasino")
elif contador ==4 or contador==3:
    print("Cumplice")
elif contador ==2 :
    print("Suspeita")
elif contador==0 or contador==1:
    print("inocente")

