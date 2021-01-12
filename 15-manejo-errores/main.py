# capturar excepciones y manejar errores en código
# susceptible a fallos/ errores
"""
try:
    nombre = input("Cuál es tu nombre? ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce tu nombre correctamente.")
else:
    print("Todo ha funcionado correctamente.")
finally:
    print("Fin de la iteración.")
"""
"""    
try:
    numero = int(input("Dime un número para elevarlo al cuadrado: "))
    print("El cuadrado es: " +str(numero*numero))
except TypeError:
    print("Debes convertir tu cadena a enteros")
except ValueError:
    print("Introduce un número correcto.")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)
"""
# excepciones "personalizadas" o lanzar excepción
try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real.")
    elif len(nombre) <= 1:
        raise ValueError("El nombre está incompleto")
    else:
        print(f"Bienvenido al Master en python {nombre}")
except ValueError:
    print("Introduce los datos correctamente.")
except Exception as e:
    print("Se ha producido un error: ", e)