from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Flavio").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/cupula_cruz.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=N)

ventana.mainloop()