class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
        
anthony = Persona("Samir", 22)

nombre = anthony.nombre
print(nombre)

anthony.nombre = "Norma"

nombre = anthony.nombre
print(nombre)
