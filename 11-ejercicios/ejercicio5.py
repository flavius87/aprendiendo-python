"""
Ejercicio 5:
Crear una lista con el contenido de esta tabla:
video juegos de ACCION  AVENTURA  DEPORTES
GTA     ASSINS               FIFA21
COD     CRASH                PRO21
PUGB    Prince of Persia     Moto GP21

Mostrar esta información ordeanada.
"""
"""
video_juegos = [
    [
    'Acción',
    'GTA',
    'COD',
    'PUGB',
    ],
    [
    'Aventura',
    'ASSINS',
    'CRASH',
    'Prince of Persia'
    ],
    [
    'Deportes',
    'FIFA21',
    'PRO21',
    'Moto GP21'
    ],
]
for video_juego in video_juegos:
    for elemento in video_juego:
        if video_juego.index(elemento) == 0:
            print("Género de video juego: " + elemento)
        else:
            print("video juego: " + elemento)
    print("\n")
"""

tabla = [
    {
        "categoría": "Acción",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoría": "Aventura",
        "juegos": ["ASSINS", "CRASH", "Prince of Persia"]
    },
    {
        "categoría": "Deportes",
        "juegos": ["FIFA21", "PRO21", "Moto GP21"]
    },
]
for categoria in tabla:
    print(f"----------{categoria['categoría']}-----------")
    for juego in categoria['juegos']:
            print(juego)
    print("\n")