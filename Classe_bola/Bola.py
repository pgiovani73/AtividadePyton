class Bola():
    def __init__(self,cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material= material
    def troca_cor(self, nova_cor):
        self.cor=nova_cor
    def mostra_cor(self):
    
        print(f"A cor da bola é {self.cor}")