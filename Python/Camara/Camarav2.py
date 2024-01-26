class Celular:
     def __init__(self, marca, modelo, camara):
         self.marca = marca
         self.modelo = modelo
         self.camara = camara

celular1 = Celular("Nokia", "m45", "56MP")
celular2 = Celular("Motorola", "Motorola g15","56MP")

print(celular2.marca)