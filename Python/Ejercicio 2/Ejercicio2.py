class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")

class Mamifero(Animal):
    def amamantar(self):
        print ("El animal esta amamamantando")

class Pinguino(Mamifero,Ave):
    pass

pinguino =Pinguino()

pinguino.comer()
pinguino.amamantar()
pinguino.volar()