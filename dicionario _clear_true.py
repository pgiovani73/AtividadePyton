#clear() - remove todos os elementos do dicionario
#tradutor1.clear()
traduto1r={}
tradutor1={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(tradutor1)
del(tradutor1["apple"]) #remove e apaga somente o elemento dentro da chave junto com indice
print(tradutor1)
print(tradutor1.pop("banana","fruta não encontrado"))
tradutor1.clear()
print(tradutor1)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# comando in prequisa a chave
tradutor1={}
tradutor1={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print("pineapple" in tradutor1)
print("pera" in tradutor1)


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# o comando in verifica apenas as chaves do dicionario, nao os valores. Para obtermos valores, podemos usar o método values()
traduto1r={}
tradutor1={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print("laranja" in tradutor1.values())

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#e posssivel alterar e substituir os elelmentos da chave
traduto1r={}
tradutor1={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(tradutor1)
tradutor1["apple"]="goiaba"
print(tradutor1)