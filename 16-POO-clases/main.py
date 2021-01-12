# Programación orientada a objetos (POO o OOP)
# Definir una clase. Es el molde para crear más objetos de ese tipo.
# Coche, con características similares.

class Coche:
    # Atributos o propiedades (variables)
    # Características del coche
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos. Son acciones que hace el objeto (coche) (funciones)

    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
# fin definición clase

# Crear objetos / Instaciar la clase
coche = Coche()

print("Coche 1: ")

coche.setColor("amarillo")
coche.setModelo("Murciélago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad nueva: ", coche.getVelocidad())

print("\n###########################################")

# Crear más objetos
coche2 = Coche()

coche2.setColor("verde")
coche2.setModelo("Gallardo")


print("Coche 2: ")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))