class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    pass

anthony = Empleado("Anthony", "22", "ecuatoriano")

print(anthony.nombre)
