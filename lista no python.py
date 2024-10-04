#listas
#uma lista (list) em pytthon e uma sequencia ou coleçã ordenada de valores
#vetores
#cada valor na lista e identificado por um indice. os valores que formam um lista sao chamados elemntos ou itens
x="ederson"
y= ["ederson", 18]
print(y)  # imprimindo os elementos dentro da lista
print("--------------------------------------------------------------------------------------")

lista1 = [10,20,30]
lista2 = ["spam", "bungee", "swallow"]
print(lista1, lista2) # a lista varias maneiras de se criar um nova lista envolvendo os elementos da lista por colchetes []
print("--------------------------------------------------------------------------------------")


lista1=["oi",2.0,5,[10.20]] # lista dentro da outra lista, ou  lista alinhadas
print (lista1)
print("--------------------------------------------------------------------------------------")


#comprimento da lista - da mesma fomra que ocorre com strings, a função len retorna o comprimento de um lista (o numero d elementos ns lista)
#ele a sublista como um unico elemento
lista1 = ["oi", 20.0,5,[10,10]]
print (len(lista1))
print("--------------------------------------------------------------------------------------")

# acessar um elemento de uma lista é a mesma usada para acessar um caractere de um strng
# utilizado o operador de indexação ([] - nao confundir com a lista vazia). A expressao dentro dos calchetes especifica o índice
numeros=[17,125,87,34,66,8398,44]
print(numeros[2])
print(numeros[9-8]) #fazendo operação dos numeros e depois ve a posição do elementos ou seja posição 1
print(numeros[-2])
print(numeros[-1])  
print("--------------------------------------------------------------------------------------")


uma_lista = [3,67,"gato",[56,57,"cachorro"],[],3.14,False] #capturando elementos dentro da lista de acordo com a posição
print(uma_lista[2][0])
print(uma_lista[3][2][0])
print("--------------------------------------------------------------------------------------")


frutas = ["maca","laranjas","bananas","cerejas"]
print("maca" in frutas)
print("pera"in frutas)
print("--------------------------------------------------------------------------------------")


uma_lista = [3,67,"gato",[56,57,"cachorro"],[],3.14,False]
print(57 in uma_lista) #apesar de existir o elemento ele nao acha ele, false
print("--------------------------------------------------------------------------------------")


#pertinencia em uma lista, concaternar
frutas = ["maca","laranjas","bananas","cereja"]
print([1,2]+[3,4])
print(frutas+[6,7,8,9])
print([]*4)
print([1,2,["ola","adeus"]]*2)
print("--------------------------------------------------------------------------------------")

