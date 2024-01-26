class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Soy un estudiante de {self.grado} grado.")



estudiante1 = Estudiante("Anthony", 22, "3ero")
estudiante1.mostrar_datos()