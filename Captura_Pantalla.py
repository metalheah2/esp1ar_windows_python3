'''
Autor : Marco Jhoel Churata Torres
Fecha :	19-08-2020
Nombre : Captura_Pantalla.py
'''

import pyautogui
import datetime
from pynput import keyboard

def tecla_press(key):
	print("Tecla presioanda == {}".format(key))
	imagen=pyautogui.screenshot()
	fecha_t=datetime.datetime.now()
	nombre_img=str(fecha_t).replace(':','.')
	imagen.save(nombre_img+".png")
	if(format(key)=="Key.esc"):
		print("Saliendo ...")
		return False
		
with keyboard.Listener(tecla_press) as listener:
	listener.join()
	