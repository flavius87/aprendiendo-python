from tkinter import *

ventana =Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Arial, 30")
    )
texto.pack()

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

"""
# El movimientro del texto hay que indicarlo dentro del pack, pero el estilo
se indica en texto.config
"""

texto = Label(ventana, text=pruebas(nombre="Flavio", apellidos="Scheck", pais="Argentina"))
texto.config(
    justify=RIGHT,
    width=400,
    height=400,
    bg="orange",
    font=("Calibri, 15"),
    cursor="spider"
    )
texto.pack()

ventana.mainloop()