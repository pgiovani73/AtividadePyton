def inverte(nome,sobrenome):
    nomeIverso = sobrenome+","+nome
    return nomeIverso
nome=input("nome: ")
sobrenome=input("sobrenome: ")
invertido=inverte(nome,sobrenome)
print("OLá", invertido)