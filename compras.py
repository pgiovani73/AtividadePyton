print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Escolhas os Produtos abaixo:")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
b=5.50
c=3.80
r=4.90
s=5.40
a=2.8
i=6.50
print(" Batata=%.2f,Cenoura=%.2f\n Beterraba=%.2f, Brocolis=%.2f\n Alface%.2f, Milho%.2f"%(b,c,r,s,a,i))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
pto=input("Escolha o Produto:")
quant=int(input("digite quantidadde:"))
vlr=float(input("digite valor do produto:"))
desc=float(input("valor do desconto:"))
vtotal=quant*vlr
desconto=vtotal*desc/100
total=vtotal-desconto
print("Valor Total sem desconto:R$",vtotal)
print("Valor Total com desconto:R$",total)