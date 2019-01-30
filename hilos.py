import psutil
import threading
import time
from colorama import init, Fore, Back, Style
import os
from random import randint

archivo = open ('datos.txt', 'w')
for proc in psutil.process_iter():
	try:
	    if proc.name() != 'cp':
	    	archivo.write(str(proc.pid)+"|"+str(proc.name())+",")
	except:
		archivo.close()
class Hilo(threading.Thread):
	def run(self):
		print('{:<10s}{:^12s}'.format(Fore.YELLOW+'INICIADO \t\t\t\t\t',self.getName()))
		time.sleep(randint(0, 8))
		print('{:<10s}{:^12s}'.format(Fore.GREEN+'TERMINADO\t\t\t\t\t',self.getName()))
os.system('clear')
archivo.close()
leer = open ('datos.txt', 'r')
cadena = leer.read()
datos = cadena.split(',')
print('--------------------------------------------------------------------------------')
print('Estado\t\t\t\t\t\t Proceso')
print('--------------------------------------------------------------------------------')
for x in datos:
    aux = x.split('|')
    hilo = Hilo(name=str(aux[1])+' - '+aux[0])
    hilo.start()
    time.sleep(randint(0, 9))


