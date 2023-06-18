from Personaje import Personaje
from Comandos import Comandos

class Inicializacion():
    
    def jugar(self):
        
        # Creación del personaje
        jugador = Personaje(None, None, None, None) #Inicializo el jugador con todo vacío
        jugador.crear_personaje() # Inicializo las propiedades del jugador (Nombre, Nivel, Vida, Ataque)
        jugador.mostrar_informacion()
        
        Comandos.esperar_tecla()
        
        
        # Historia introductoria
