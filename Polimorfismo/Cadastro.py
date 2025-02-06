class Pessoa():
    def __init__(self):
        self.nome=input("digite nome:")
        self.endereco=input("digite endereço:")
        self.fone=int(input("digiete o telefone:"))

class Empresa(Pessoa):
    def pj(self):
       self.cnpj=int(input("digite CNPJ:"))
       self.ie=input("digite inscrição estadual:")
       
class Pessoal(Pessoa):
    def pf(self):
       self.cpf=int(input("digite cpf:"))
       self.rg=input("digite RG:")
