class Pessoa():
    def __init__(self,nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso= peso
        self.altura=altura
    def idade1(self, nova_idade):
        self.idade+=nova_idade
        print(f"A nova idade é: {self.idade}")
    

       