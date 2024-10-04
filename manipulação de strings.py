# manipulação de strings
a=" pedro "
print(len(a)) # função - len - 
b=(len(a))
print(b)

# como "capitalizar" (transforma a primeira letra em maiuscula)
a = "ederson"
print(a.capitalize()) # função - capitalize -

# como transfomrar todo o texto em maiusculo.
a="ederson"
print(a.upper())

#transoformar todo o texto em minusculo.
a = "EDERSON"
print(a.casefold())

print("EDERSON".upper()) # SEGUNDA FORMA DE TRANSFORMAR EM MINUSCULO

a= "EDERSON"
print(a.islower()) # identifica se o texto esta em minusculo - FALSE -

A="ederson"
print(a.islower()) # identifica se o texto esta em minusculo - TRUE -

A="EDERSON"
print(a.isupper()) # identifica se o texto esta em minusculo - TRUE -

a= "12345"
print(a.isdigit()) #verificar se a string e totalmente Inteiro

a= "1234abc5"
print(a.isdigit()) #verificar se a string e totalmente Inteiro

a = "Ederson Roberto"
print(a.replace("Roberto","Costa")) # o metodo replace serve para trocar todas as ocorrencias de uma sbstring por outra string

a="Ederson-Roberto-Costa"
print(a.split("-")) # subistui os parametro de sepração por virgula = retorna um lista das substrings, se passado sem parametro subtitui por "," ou substitui o paramentro por ","
a="Ederson Roberto Costa"

print(a.find("Costa"))
x="abcdefgh"
print(x.find("f")) # a função find retorna onde a substring começa na string, o posião começa no 0,1,2,3,4...

a="Pedro Giovani Teixeira"
print("Teixeira"in a) # o operador "in" verifica se uma substring e parte de uma outra string

a="Pedro Giovani Teixeira"
print(a.count("o")) # o operador "count" retorna a frquencia de ocorrencia do paramentro pedido

s="Olá, mundo!"
print(s[0])
print(s[2])
print(s[6]) # esse comando "s" serve para printar a variavel noa posição solicitada

x="Olá, mundo!"
print(x[-11])
print(x[-9])
print(x[-5])

s="Olá, mundo!"
print(s[1:3]) # o índice de ínicio da fatia ou o de final [ou ambos], o ínicio e o final da string serão considerados, respectivamente

s="olá. mundo!"
print(s[:3]) # Se omitimos o índice de ínicio da fatia ou o de final [ou ambos], o ínicio e o final da string serão considerados, respectivamente