# declaraç~çao de função no python
def hello():
    print ("Olá!!")

hello() # chamar uma função? chama pelo nome,

# so depois que chamamos a função (hello), e que acontece algo, Ou seja, o Python pula esses def,
#nao roda ele de cara. alias , se voce nao tivesse chamdo a função via Hello(). aquele codigo nem seria executado


# colocar um parametro insire uma variavel, a álavra def, na primeira linha, explica a definição da função naquele ponto. 
# Emseguida, entre parenteses, teremos o parametro NOME que recebera uma string
def hello(nome):
    print ("OLá", nome)
hello("Pedro Giovani")


# passagem de parametro

def hello(nome):
    print("seja bem vindo", nome)
a=input("Digite seu nome: ")

hello(a)
a=input("Digite seu nome: ")
hello(a)
a=input("Digite seu nome: ")
hello(a)
a=input("Digite seu nome: ")
hello(a)
