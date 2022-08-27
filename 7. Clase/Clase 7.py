import tkinter as tk
from tkinter import *
from tkinter import filedialog
from BotPOO import Bot
from datetime import datetime

def iniciarBot():
    objetoBot=Bot(telefono=cajaNumero.get(),mensaje=cajaMensaje.get())
    objetoBot.abrirWhatsApp()
    objetoBot.enviarMensaje()
    guardarNumero()
    guardarMensajes()
    generarHistorial()

def abrirArchivo():
    direccionImagen=filedialog.askopenfilename(title="Abrir archivo")
    objetoBot=Bot(telefono=cajaNumero.get(),ruta=direccionImagen)
    objetoBot.abrirWhatsApp()
    objetoBot.enviarArchivo()
    print(direccionImagen)

def guardarNumero():
    fichero = open("numeros.txt", "a")
    fichero.write(cajaNumero.get()+"\n")
    fichero.close()

def guardarMensajes():
    fichero = open("mensajes.txt", "a")
    fecha = datetime.now()
    fichero.write(cajaMensaje.get()+"\nEnviado a:"+cajaNumero.get()+" un "+str(fecha.date())+" a las "+str(fecha.time().strftime("%H:%M:%S"))+"\n")
    fichero.close()
def generarHistorial():
    cajaTextoNumeros.configure(state='normal')
    cajaTextoMensajes.configure(state='normal')
    cajaTextoNumeros.delete("1.0","end")
    cajaTextoMensajes.delete("1.0","end")
    ficheroNumeros=open("numeros.txt", "r")
    cajaTextoNumeros.insert(1.0,ficheroNumeros.read())
    cajaTextoNumeros.configure(state='disabled')
    ficheroMensajes=open("mensajes.txt", "r")
    cajaTextoMensajes.insert(1.0,ficheroMensajes.read())
    cajaTextoMensajes.configure(state='disabled')


ventana = tk.Tk()
ventana.title("Bot WhatsApp")
ventana.config(width=900, height=500)


labelNumero = Label(text="Ingresa numero telefono")
labelNumero.place(x=20, y=20)
labelMensaje = Label(text="Ingresa mensaje")
labelMensaje.place(x=20, y=60)

cajaNumero = Entry()
cajaNumero.place(x=200, y=20, width=100)

cajaMensaje = Entry()
cajaMensaje.place(x=200, y=60, width=100)

botonEnviar = Button(text="Enviar", command=iniciarBot,activebackground="red")
botonEnviar.place(x=320, y=60)

botonAbrir= Button(text="Abrir archivo", command=abrirArchivo,activebackground="red")
botonAbrir.place(x=20, y=100)

labelNumeros = Label(text="Numeros registrados")
labelNumeros.place(x=20, y=150)

cajaTextoNumeros = Text()
cajaTextoNumeros.place(x=20, y=200,height=300, width=200)

labelNumeros = Label(text="Mensajes enviados")
labelNumeros.place(x=300, y=150)

cajaTextoMensajes = Text()
cajaTextoMensajes.place(x=300, y=200,height=300, width=500)

generarHistorial()

ventana.mainloop()