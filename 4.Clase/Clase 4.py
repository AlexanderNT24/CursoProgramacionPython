#1
import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.mainloop()
#2
import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.config(width=400, height=300)
label = ttk.Label(text="Hola a todos")
label.place(x=20, y=20)
ventana.mainloop()
#3
import tkinter as tk
from tkinter import ttk

def sumar():
    labelSaludo=ttk.Label(text="Hola "+cajaTexto.get())
    labelSaludo.place(x=20, y=100)
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.config(width=400, height=300)
label = ttk.Label(text="Ingresa nombre")
label.place(x=20, y=20)

cajaTexto = ttk.Entry()
cajaTexto.place(x=140, y=20, width=60)
boton = ttk.Button(text="Saludar", command=sumar)
boton.place(x=20, y=60)
ventana.mainloop()
#4 
import tkinter as tk
from tkinter import ttk

def sumar():
    suma=(float(cajaNumero1.get())+float(cajaNumero2.get()))
    labelSaludo=ttk.Label(text=suma)
    labelSaludo.place(x=20, y=100)
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.config(width=400, height=300)

label1 = ttk.Label(text="Ingresa primer numero")
label1.place(x=20, y=20)
label2 = ttk.Label(text="Ingresa segundo numero")
label2.place(x=20, y=40)

cajaNumero1 = ttk.Entry()
cajaNumero1.place(x=160, y=20, width=60)

cajaNumero2 = ttk.Entry()
cajaNumero2.place(x=160, y=40, width=60)
boton = ttk.Button(text="Sumar", command=sumar)
boton.place(x=20, y=60)
ventana.mainloop()