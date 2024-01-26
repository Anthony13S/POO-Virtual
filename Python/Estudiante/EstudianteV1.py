class Estudiante:
    def __init__(self, nombre,edad,grado):
         self.nombre = nombre
         self.edad = edad
         self.grado = grado

anthony = Estudiante("Anthony", "22", "5to")

print(anthony.grado)