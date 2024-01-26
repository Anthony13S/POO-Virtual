class Persona:
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

anthony = Persona("Samir",22)
     
nombre = anthony.get_nombre()
print(nombre)


anthony.set_nombre("Tampico")

nombre = anthony.get_nombre()
print(nombre)