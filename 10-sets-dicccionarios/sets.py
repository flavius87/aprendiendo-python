"""
Un set es un dato para tener una colección de valores que no tiene 
indice ni orden.
"""

persona = {
    "Victor",
    "Manolo",
    "Francisco"
}

persona.add("Paco")
persona.remove("Francisco")

print(type(persona))
print(persona)