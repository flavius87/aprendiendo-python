"""
Tkinter: modulo para crear interfaces gráficas de usuario.
"""
from tkinter import *
import os.path

class Programa:
# constructor
    def __init__(self):
        self.title = "Interfaz gráfica con Python by Flavio Scheck"
        self.icon = './imagenes/logo.ico'
        self.icon_alt = './21-tkinter/imagenes/logo.ico'
        self.size = "750x450"
        self.resizable = False
    
    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Crear título
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0) 


    def addTexto(self):
        texto = Label(self.ventana, text="Hola a todos")
        texto.pack()

    def mostrar(self):
         # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instaciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto()
programa.mostrar()