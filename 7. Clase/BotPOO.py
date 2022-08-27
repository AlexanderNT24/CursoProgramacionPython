import webbrowser,pyautogui
from time import sleep

class Bot:
    def __init__(self,telefono,mensaje='',ruta=''):
        self.telefono=telefono
        self.mensaje=mensaje
        self.ruta=ruta

    def abrirWhatsApp(self):
        webbrowser.open('https://api.whatsapp.com/send?phone='+str(self.telefono))
        sleep(5)

    def enviarMensaje(self):
        pyautogui.typewrite(self.mensaje)
        pyautogui.press('enter')
        sleep(1) 

    def enviarArchivo(self):
        
        fichero=open(self.ruta, "r")

        for line in fichero:
            pyautogui.typewrite(line)
            pyautogui.press('enter')

            sleep(1)

