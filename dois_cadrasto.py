def cadastro():
    name=input("Qual seu nome: ")
    age=int(input("Idade"))
    return name, age

print ("Iniciando Cadastro")
nome,idade = cadastro()
print("Cadastro realizado com sucesso:")
print("Seu nome é",nome,"e você tem",idade,"anos de idade")