class Personaje:
    def __init__ (self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__ (self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_PJ):
        nuevo_nombre = self.nombre + "-" + otro_PJ.nombre
        nueva_fuerza = round(((self.fuerza + otro_PJ.fuerza)-2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_PJ.velocidad)/2)**1.5)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
ursa = Personaje("Ursa", 100, 100)
lina = Personaje("Lina", 90, 90)
tinker = Personaje("Tinker", 200, 200)

ursina = ursa + lina
tinkersa = tinker + ursa

print(tinkersa)
print(ursina)
print(ursa)
print(lina)
print(tinker)
