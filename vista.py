import tkinter as tk
from tkinter import *

#Creamos las ventanas
root = tk.Tk()

#Creamos la etiqueta
widget = Label(None, text='Hola Mundo tkinter')
#Agregamos la etiqueta a la ventana
widget.pack()
#Modificamos el tamaño de la ventana
root.geometry("800x800")
#Ciclo de espera de eventos
root.mainloop()