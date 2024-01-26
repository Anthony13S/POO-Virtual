class Celular:
    def __init__(self, marca, modelo, camara):
         self.marca = marca
         self.modelo = modelo
         self.camara = camara

    def llamar(self):
     print(f"Estas haciendo una llamada desde un :{self.modelo}")
     
    def cortar(self):
     print(f"Cortaste la llamada desde un :{self.modelo}")

celular1 = Celular("Nokia", "m45", "56MP")
celular2 = Celular("Motorola", "Motorola g15","56MP")

celular2.llamar()

