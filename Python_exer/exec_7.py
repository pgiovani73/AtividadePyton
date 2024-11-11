def conta_vogais(texto):
    vogais= "aeiouAEIOU"
    contador=0
    for letra in texto:
        if letra in vogais:
            contador=contador+1
    return contador
texto=input("digite um texto: ")
print(conta_vogais(texto))