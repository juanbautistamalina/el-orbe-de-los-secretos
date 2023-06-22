from Personaje import *
from Comandos import *
from Historia import * 

"""
    Clase Inicialización: En esta clase, existe un método llamado jugar el cual se encarga de 
    crear una instancia de la clase Personaje, aplicarle el método crear_personaje el cual inicializa las propiedades
    del jugador y posteriormente las muestra por consola. 
    
    Luego de esperar que el usuario pulse una tecla, se crea una instancia de la clase Historia, esto con el objetivo de
    pasarle por parámetros el nombre del jugador para que así pueda mostrar por consola un texto introductorio.
    
    Luego se llama al método estático iniciar_cap1() de la clase Comandos.
    
"""

class Inicializacion():
    
    @staticmethod
    def jugar():
        
        # Creación del personaje
        jugador = Personaje(None, None, None, None) # Inicializo el jugador con todo vacío
        jugador.crear_personaje() # Inicializo las propiedades del jugador (Nombre, Nivel, Vida, Ataque)
        jugador.mostrar_informacion() # Muestro la información del jugador por consola
        
        Comandos.esperar_tecla(True)
        
        # Mostrando la Historia Introductoria
        historia = Historia()
        historia.introduccion(jugador.get_nombre())
        
        # Inicia el Capítulo 1
        Comandos.iniciar_cap1()