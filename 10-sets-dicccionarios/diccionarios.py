"""
Un diccionario es un tipo de dato que almacena un conjunto de datos
en formato clave > valor
Es parecido a un array asociativo o a un objeto json
"""

persona = {
    "nombre": "Flavio",
    "apellido": "Scheck",
    "web": "flavioscheck.com"
}

print(persona["apellido"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Guillermina',
        'email': 'guillermina@hotmail.com'
    },
    {
        'nombre': 'Tato',
        'email': 'eltato@yahoo.com.ar'
    }
]

contactos[0]['nombre'] = 'Gervasio'
print(contactos[0]['nombre'])

print("\nLISTADO DE CONTACTOS: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
print("\n")
