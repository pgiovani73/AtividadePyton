def soma_lista(lista):
  soma = 0
  for numero in lista:
    soma+=numero
  return soma
minha_lista = [1,3,4,5,6]
resultado=soma_lista(minha_lista)
print (resultado)

print(sum(minha_lista))