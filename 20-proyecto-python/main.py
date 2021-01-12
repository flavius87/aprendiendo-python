"""
Proyecto python mysql: 
-Abrir asistente
-Login o registro
-Si elegimos registro, nos meterá en una base de datos
-Si elegimos login, identifica al usuario y nos preguntará qué queremos hacer
-Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -login
    -registro
""")

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
    