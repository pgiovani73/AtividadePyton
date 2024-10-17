while True:
    user=(input("Usuario:"))
    senha=(input("Digite a Senha: "))


    if senha==user:
        print("--senha invalida--")
    elif senha != user:
        print("---ACESSO PERMITIDO---")
        break
    