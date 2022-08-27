import tkinter as tk
from tkinter import *
from tkinter import filedialog
from BotPOO import Bot

def iniciarBot():
    objetoBot=Bot(telefono=cajaNumero.get(),mensaje=cajaMensaje.get())
    objetoBot.abrirWhatsApp()
    objetoBot.enviarMensaje()
    labelAviso=Label(text="Mensaje enviado")
    labelAviso.place(x=20, y=150)
def abrirArchivo():
    direccionImagen=filedialog.askopenfilename(title="Abrir archivo")
    objetoBot=Bot(telefono=cajaNumero.get(),ruta=direccionImagen)
    objetoBot.abrirWhatsApp()
    objetoBot.enviarArchivo()
    print(direccionImagen)

ventana = tk.Tk()
ventana.title("Bot WhatsApp")
ventana.config(width=400, height=300)

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


ventana.mainloop()
