from Personaje import *
from Comandos import *
from Historia import * 


class Inicializacion():
    
    def jugar(self):
        
        # Creación del personaje
        jugador = Personaje(None, None, None, None) #Inicializo el jugador con todo vacío
        jugador.crear_personaje() # Inicializo las propiedades del jugador (Nombre, Nivel, Vida, Ataque)
        jugador.mostrar_informacion()
        
        Comandos.esperar_tecla(True)
        
        # Mostrando la Historia Introductoria
        historia = Historia()
        historia.introduccion(jugador.get_nombre())
        
        # Inicia el Capítulo 1
        Comandos.iniciar_cap1()