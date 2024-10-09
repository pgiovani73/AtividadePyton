vl1=(int(input("Digite um valor:")))
vl2=(int(input("Digite outro valor:")))
vl3=(int(input("Digite mais um valor")))
if vl1>vl2 and vl2>vl3:
    print(vl3,vl2,vl1)
elif vl1>vl3 and vl3>vl2:
    print(vl2,vl3,vl1)
elif vl2>vl1 and vl1>vl3:
    print(vl3,vl1,vl2)
elif vl2>vl3 and vl3>vl1:
    print(vl1,vl3,vl2)
elif vl3>vl1 and vl1>vl2:
    print(vl2,vl1,vl3)
elif vl3>vl2 and vl2>vl1:
    print(vl1,vl2,vl3)
    