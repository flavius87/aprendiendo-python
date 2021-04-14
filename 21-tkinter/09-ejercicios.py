"""
CALCULADORA
-Dos campos de texto
-4 botones para las operaciones
-Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox 
import os.path

ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=25)
ventana.title("Calculadora")

ventana.iconbitmap('./21-tkinter/imagenes/calculadora.ico')

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0 
        messagebox.showerror("Error", "Introduce datos numéricos")
    return result

def sumar():
    resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
    mostrarResultado()
    
def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID,
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
# Campo de texto
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
# Campo de texto
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

# Cuatro botones
Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()