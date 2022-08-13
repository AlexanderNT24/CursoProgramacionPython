import webbrowser,pyautogui

from time import sleep

webbrowser.open('https://api.whatsapp.com/send?phone=51955516189')

sleep(5)

fichero=open("archivo.txt", "r")


for line in fichero:
    pyautogui.typewrite(line)
    pyautogui.press('enter')
    sleep(1)