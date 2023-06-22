
"""
    Clase Personaje: En esta clase se inicializan las propiedades comunes de los personajes 
    de la cual, van a heredar las clases Jugador y Enemigo. 
    
    - crear_personaje(): Este método ermite que el usuario introduzca su nombre de usuario y lo corrija 
    en caso de desearlo. Además le da por defecto el nivel = 1, vida = 100, ataque = 20
    
    - mostrar_información(): Este método le muestra por consola al usuario los siguientes datos: 
    Nombre, Nivel, Vida y Ataque.
    
    - get_nombre(): Este método retorna el nombre del usuario (Se utiliza principalmente para el método introducción
    de la clase Historia)
    
"""
class Personaje(): 
    
    def __init__(self, nombre, nivel, vida, ataque):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        
        #self.ARMA
        #self.INVENTARIO
    
    
    
    def crear_personaje(self):
    
        # Confirmación de nombre de usuario
        while True: 
            self.nombre = input("¡Bienvenido al juego! Por favor, introduce el nombre de tu personaje: ")
            confirmacion = input(f"¿Estás seguro de que quieres nombrar a tu personaje '{self.nombre}'? (S/N): ")

            if confirmacion.lower() == "s" or confirmacion.lower() == "si":
                print(f"¡Excelente, {self.nombre}! Tu personaje ha sido creado.")
                print("────────────────────────────────────────────────────────────────────────────────────────────────")
                
                # Inicializando propiedades
                self.nivel = 1
                self.vida = 100
                self.ataque = 20
                
                return Personaje(self.nombre, self.nivel, self.vida, self.ataque) 
                
                # Sale del bucle si la confirmación es 's' (sí)
        
            elif confirmacion.lower() == "n" or confirmacion.lower() == "no":
                print("Entendido, puedes editar el nombre de tu personaje.")
                continue  # Vuelve a solicitar el nombre de usuario
        
            else:
                print("Respuesta inválida. Por favor, responde 'S' para sí o 'N' para no.")
        
    
    def mostrar_informacion(self):
        print("Tus datos de personaje son: \n")
        print("⦿  Nombre: ", self.nombre)
        print("⦿  Nivel: ", self.nivel)
        print("⦿  Vida: ",self.vida, "HP")
        print("⦿  Ataque: ",self.ataque)
        print("────────────────────────────────────────────────────────────────────────────────────────────────")
        
    
    def get_nombre(self):
        return self.nombre