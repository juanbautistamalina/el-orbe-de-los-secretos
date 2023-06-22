import time
from Historia import *

"""
    Clase Comandos: Esta clase posee 3 comandos estáticos
    
    - esperar_tecla(): Espera que el usuario presione una tecla para continuar la ejecución del juego
    
    - efecto_delay(): Este método produce un efecto de delay a todo texto que se le pase por parámetros, permitiendo
    también colocar en los parámetros, la velocidad a la que aparecerá el texto por pantalla.
    
    - iniciar_cap1(): Este método guarda en una variable lo que le devuelve el método get_titulo de la clase historia,
    al cual se le pasa por parámetros el número 1 para que así, lo que retorne sea el título del capítulo 1.
    También se hace uso del método efecto_delay, en el que se le pasa por parámetros, primero el título antes
    mencionado, y luego la velocidad a la que va a aparecer. 
    Finalmente, este método llama a otro método llamado esperar_tecla para que el usuario pulse una tecla y el programa
    continúe con su ejecución. 

"""


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