class Vendedor():
    def__init__(self, nome, vendas): #quando estaos creiando um classse, a primeira coisas e definir um a função __init__criar clase init com fução medtodo construtor
        self.nome = nome # self.nome ese torna uma variavel global
        self.vendas = vendas
vendedor1 = Vendedor("pedro",1000)
print(vendedor1.nome)    