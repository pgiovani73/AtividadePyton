def eh_palindromo(p):
    p = p.replace(" ", "").lower()  
    return p == p[::-1]
pa=input("digite um texto: ")

print(eh_palindromo(pa))  