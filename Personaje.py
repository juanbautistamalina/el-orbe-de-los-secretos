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
                break  # Sale del bucle si la confirmación es 's' (sí)
        
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
        
    