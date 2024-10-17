while True:
    nome=(input("Digite o nome:"))
    if (len(nome))>=3:
        print("Nome:",nome)
        break
    else:
        print("digite acima de 2 caracteres")

while True:
    idade=int(input("Digite a idade:"))
    if idade >=0 and idade <=150:
        print("idade:",idade)
        break
    else:
        print("digite entre abaixo de 150")

while True:
    salario=float(input("Digite o salario:R$"))
    if salario >=0:
        print("salario:R$",salario)
        break
    else:
        print("digite salario maior que zero")

while True:
    sexo=(input("digite f -feminino, m -masculino, o -outros\n"))
    if sexo=="o" or sexo =="f" or sexo == "m":
        print(sexo)
        break
    else:
        print("digite uma opção valida")

