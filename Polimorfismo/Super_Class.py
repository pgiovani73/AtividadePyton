class Super:
    def hello(self):
        print("Ola, sou a super classe")
    def printar(self):
        print("Ola, sou a outra Clase!...")
class Sub (Super):
    def hello(self):
        print("ola, sou a subclasse!")

class Subsub (Sub):
    def hello (self):
        print("Olá, sou a subsubclasse!")
teste=Super()
teste.printar()
teste.hello()

teste=Sub()
teste.hello()

teste=Subsub()
teste.hello()
teste.printar()

    
