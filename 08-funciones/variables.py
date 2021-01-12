"""
variables locales: se definen dentro de la función 
y no se puede usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos return.

variables globales: se declaran fuera de una función y están disponibles
dentro y fuera de ellas.
"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres."

print(frase) 

def holamundo():
    frase = "Hola mundo"
    print("Dentro de la función.")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "victorroblesweb.es"
    print("Dentro: ", website)

holamundo()
print("Fuera: ", website)
