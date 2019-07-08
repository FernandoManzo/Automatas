# Nombre: calculadora.py
# Objetivo: calculadora básica
# Author: Fernando Manzo Virgen
# 06/07/2019

from tkinter import *

def imprimir():
    n1.set("")
    n2.set("")

def borrar():
    n1.set("")

def salir():
    print()

# Configuración de la raíz
root = Tk()
root.title("Ejercicio 7")
root.config(bd=30)

n1 = StringVar()


Label(root, text="Texto").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="").pack()  # Separador

Button(root, text="Imprimir", command=imprimir, fg="white", bg="green").pack(side="left")
Button(root, text="Borrar", command=borrar, fg="white", bg="orange").pack(side="left")
Button(root, text="Salir", command=salir, fg="white", bg="blue").pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()
