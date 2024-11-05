# e possivel criar um dicionario dentro de uma chave de um dicionario
dados={}
dados={"crossfox":{"km":"35000","ano":"2005"},"DS":{"km":"17000","ano":"2015"},"fusca":{"km":"13000","ano":"1979"},"Jetta":{"km":"5600","ano":"2011"},"passat":{"km":"62000","ano":"1999"}}
print(dados)
print (dados["fusca"]["ano"])

# os dicionarios possuem metodo de especifico para busca de valores, o get(), no qual podemos passar como paramtros a chave que queremos e um valor padrao
# para retornar caso essa chave nao seja encontrda
print(dados.get("gol", "veiculo nao encontrado"))