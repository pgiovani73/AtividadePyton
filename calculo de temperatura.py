#faça u programa que contenha duas temperaturas por mes, uma em cada lista de todos os mese do ano. apos isto, calcule a meida anual das temperaturas, mostre a mairo e amenos. imprimir em ordem crescente e decrescente.
#nao utilizar as mesmas temperaturas
jan=[28,41]
fev=[34,36]
mar=[29,18]
abr=[35,19]
mai=[17,26]
jun=[20,31]
jul=[22,33]
ago=[31,42]
set=[43,16]
out=[30,37]
nov=[43,15]
dez=[23,27]
print(jan,fev,mar,abr,mai,jun,jul,ago,set,out,nov,dez)
temp=[]
temp.extend(jan)
temp.extend(fev)
temp.extend(mar)
temp.extend(abr)
temp.extend(mai)
temp.extend(jun)
temp.extend(jul)
temp.extend(ago)
temp.extend(set)
temp.extend(out)
temp.extend(nov)
temp.extend(dez)
print("temperatura dos ultimos 12 meses",temp)
media=sum(temp)/len(temp)
print("temperatura media",media)
maior=max(temp)
print("maior temperatura",maior)
menor=min(temp)
print("menore temperatura",menor)