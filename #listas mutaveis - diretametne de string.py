#listas mutaveis - diretametne de strings, listas são mutaveis (mutable)
#combinando ma atribuição com operador de fatiamento, tipo trocando os elemetos dentro variavel
frutas = ["banana","maça", "cereja"]
frutas[0]="pera"
frutas[-1]="laranja"
print(frutas)

print ("\n-------------------------------------------------------------\n")

uma_lista =["a","B","c","d","e","f"] #combinando uma atribuição com o operador de fatiamento podemos atualizar varios elementos
uma_lista[1:3]=['x','y']
print(uma_lista)

print ("\n------------------------------------------------------------\n")

uma_lista =["a","B","c","d","e","f"] 
print(uma_lista)
print(len(uma_lista))
uma_lista [1:3]=[]
print(uma_lista)
print(len(uma_lista))

print ("\n------------------------------------------------------------\n")

uma_lista =["a","d","f"] #podemos inserir um elementos nas posiçoes marcadas
uma_lista [1:1]=['b','c']
print(uma_lista)
uma_lista[4:4]=['e']
print(uma_lista)

print ("\n------------------------------------------------------------\n")

a=['um','dois','tres']#apagar elementos de uma lista
del a[1]
print(a)
lista =["a","B","c","d","e","f"] 
del lista[1:5]
print(lista)

print ("\n------------------------------------------------------------\n")

a=[81,82,83] # adiconar elemto ao final da lista
a.append(5)
print (a)

print ("\n------------------------------------------------------------\n")

#lista.sort(reverse=true) ordenar os valores de ordem reversa ou decrecente
#reverse e um metodo de lista que inverte a ordem da lista, mas nao ordena.
a=[88,81,82,83]
a.sort()
print(a)

print ("\n------------------------------------------------------------\n")

#index mostra qual posiçao qeu o elemento esta
a=[1,2,3,4,5,6,7,8,9]
print (a.index(4))

print ("\n------------------------------------------------------------\n")

#insert e uma metoedo de listas que insere o valor na posição desejada. informa a posição e posteriormente o valor
a=[88,81,82,83]
a.insert(1,100) #posição insira 100
print(a)

print ("\n------------------------------------------------------------\n")      

#pesquisa quantas veses aperece o mesmo elemento na lista
a=[88,81,82,83,88,85,88,86]
print(a)
print(a.count(88))

print ("\n------------------------------------------------------------\n") 

a=[88,81,82,83,88,85,88,86]
a.pop()#apaga o ultimo elemento
print(a)
a.pop(0)#apaga a posição informada
print(a)

print ("\n------------------------------------------------------------\n")

#extend acrescenta os elementos de lista ao final da lista, mais de uma lista
listas=[1,2]
listas.extend([3,4,5])
print(listas)

print ("\n------------------------------------------------------------\n")
