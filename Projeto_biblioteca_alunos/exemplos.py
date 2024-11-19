import numpy as np

# array_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]) 
# print(array_3d)

# x = np.linspace(0, 1, 10) 
# print(x)

# array_aleatorio=np.random.rand(10,2)
# print("array aleatorio", array_aleatorio,)

# n=np.array([[1,71,30,4,5], [4,57,65,41,10]])
# print(n)
# print("soma",n.sum())
# print("media",n.mean())
# print("valor maximo",n.max()) 
# print("valor minimo",n.min())


n = np.arange(10)
print(n)  

n = np.arange(2, 11, 2)
print(n)  

array_aleatorio = np.random.rand(10) 

soma = np.sum(array_aleatorio) 

media = np.mean(array_aleatorio) 

maximo = np.max(array_aleatorio) 

minimo = np.min(array_aleatorio) 

  

print("Array aleatório:", array_aleatorio) 

print("Soma:", soma) 

print("Média:", media) 

print("Máximo:", maximo) 

print("Mínimo:", minimo) 

matriz = array_aleatorio.reshape(2, 5) 

print("Matriz reshape:", matriz) 