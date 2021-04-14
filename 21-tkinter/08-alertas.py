from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    Messagebox.showinfo("Alerta", "Hola, soy Flavio Scheck")

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = Messagebox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")
    if resultado != "yes":
        Messagebox.showinfo("Chau", f"Adiós {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Flavio Scheck")).pack()

ventana.mainloop()

