class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        return ("Hola, yo hablo poco")

class Artista:
    def __init__(self,talento):
        self.talento = talento

    def mostrar_talento(self):
        return (f"Mi talento es: {self.talento}")



class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,talento,empresa,salario ):
       Persona.__init__(self,nombre,edad,nacionalidad)
       Artista.__init__(self,talento)
       self.salario = salario
       self.empresa = empresa


    def presentarse(self):
        print (f"Hola me llamo: {self.nombre} y {self.mostrar_talento()} y trabajo de {self.empresa}")


anthony = EmpleadoArtista("Anthony","22","ecuatoriano","bailar","entregador","Ecuadis")

anthony.presentarse()