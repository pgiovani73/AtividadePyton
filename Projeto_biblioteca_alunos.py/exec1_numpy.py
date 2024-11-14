# criar array uma função de array aleatorio com 5 linhas e 2 colunas
import numpy as np
array_aleatorio=np.random.rand(10).reshape(5,2)
print("array aleatorio", array_aleatorio,"\n")

#crair uma matriz dimensional com os seguinte numeros abaixo e depois soma a matriz;
#x= 10,21,32,4,5 e 4,57,65,41,10
x=np.array([[1,2,3,4,5], [4,57,65,41,10]])
print(x)
print(x.sum())
print(x.mean())
print(x.max()) 
print(x.min(),"\n")
#m edia=np.mean(array) 
# soma=np.sum(array)
# valor maximo da matriz=np.max(array) e valor minmo = np.min(array)


#Criar um array 3D com 3 camadas, cada uma com 3 dimensões, 
a=np.arange(27).reshape(3,3,3)
print(a)
print(a.ndim) # indica numeros de dimensoes e camadas

matriz=array_aleatorio.resahpe(5,2)
print(matriz)
