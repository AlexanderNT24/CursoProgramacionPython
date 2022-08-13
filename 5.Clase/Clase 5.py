fichero=open("archivo.txt", "r")
print(fichero.read())

fichero = open("archivo.txt", "a")
fichero.write("Ahora tiene mas contenido")
fichero.close()

fichero = open("archivo.txt", "w")
fichero.write("Se eliminó el contenido anterior y se creó uno nuevo")
fichero.close()

import webbrowser

webbrowser.open('https://docs.python.org/3/library/webbrowser.html')

import pyautogui
#Posicion del mouse
posicionMouse=pyautogui.position()
print(posicionMouse)
#Mover el mouse a una coordenada
pyautogui.moveTo(300, 200)
#Presionar y soltar una tecla
pyautogui.press("a")
pyautogui.press("enter")
#Escribir un texto 
pyautogui.typewrite("Hola me controlo solo :D")