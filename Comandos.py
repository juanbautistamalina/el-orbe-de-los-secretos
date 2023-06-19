import time
from Historia import *

class Comandos():
    
    @staticmethod
    def esperar_tecla(linea):
        input("Presiona cualquier tecla para continuar... \n")
        
        if(linea == True):
            print("────────────────────────────────────────────────────────────────────────────────────────────────")

    @staticmethod
    def efecto_delay(text, delay):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
    
    @staticmethod
    def iniciar_cap1():
        titulo = Historia.get_titulo(1)
        Comandos.efecto_delay(titulo, 0.01)
        Comandos.esperar_tecla(False)
        
        
        #Historia.cap_1()