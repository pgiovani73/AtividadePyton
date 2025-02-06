# Classe TV: FAça um programa que simule um televisor criando-o como um objeto. O usuário dever ser capaz de informar o número do canal e aumentar ou diminuir o volumoe.
# certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas

class Tv:
    def __init__(self, canal, volume,):
        self.canal=["canal1","canal2","canal3","canal4"]
        self.canal_atual="canal1"
        self.canal1=["canais"]
        self.volume=volume
       
    def aumentar_volume(self):
        if self.volume>self.volumeMais:
            self.volume+=1
            print(f'Volume aumentado para {self.volume}')
        else:
             print("Volume màximo atingido !")
       
    def diminuir_volume(self):
        if self.volume<self.volumeMenos:
            self.volume=1
            print(f'Volume diminuido para {self.volume}')
        else:
             print("Volume minimo atingido !")

    def aumentar_canal(self):
        if self.canal_atual>self.canalMais:
            self.canalMais+=1
            print(f'Canal Atual {self.canal}')
        else:
             print("Canal màximo atingido !")

