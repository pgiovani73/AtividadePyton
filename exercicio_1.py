ponto_a1=float(input("Digite ponta A1:"))
ponto_a2=float(input("Digite ponta A2:"))
ponto_b1=float(input("digite ponto B1:"))
ponto_b2=float(input("Digite ponta B2:"))

d=(ponto_b1-ponto_a1)**2+(ponto_b2-ponto_a2)**2
x=d**(1/2)
print(f"{x:.2f}")
