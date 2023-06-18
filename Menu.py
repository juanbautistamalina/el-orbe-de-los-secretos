# Importo del archivo Inicialización.py la clase Inicializacion
from Inicializacion import *


class Menu():
    
    # Este menú será visual en un futuro:
    @staticmethod 
    def mostrar_menu(): 
        print("╔═════════════════════════════════════════════╗")
        print("║           EL ORBE DE LOS SECRETOS           ║")
        print("╠═════════════════════════════════════════════╣")
        print("║                                             ║")
        print("║            1. Jugar                         ║")
        print("║                                             ║")
        print("║            2. Instrucciones                 ║")
        print("║                                             ║")
        print("║            3. Créditos                      ║")
        print("║                                             ║")
        print("║            4. Salir                         ║")
        print("║                                             ║")
        print("╚═════════════════════════════════════════════╝")


    @staticmethod 
    def seleccion_menu(): 
        
        # Instancia de la clase Inicialización para poder crear el personaje del usuario
        inicializacion = Inicializacion()
        
        
        while True: 
            Menu.mostrar_menu()
            
            opcion = input("Selecciona una opción: ")
            opcion = opcion.lower()
            print("────────────────────────────────────────────────────────────────────────────────────────────────")
    
            if opcion == "jugar" or opcion == "1":
                
                Menu.frase_bienvenida()
                print("────────────────────────────────────────────────────────────────────────────────────────────────")
                inicializacion.jugar()
                break
    
            elif opcion == "instrucciones" or opcion == "2":
                print("╔═══════════════════════════════════════════════════════════════════╗ ")
                print("║    Aquí tienes las instrucciones para que puedas disfrutar        ║ ")
                print("║          de esta emocionante experiencia:                         ║")
                print("╠═══════════════════════════════════════════════════════════════════╣")
                print("║ 1. Toma de Decisiones: En diferentes momentos del juego, se       ║")
                print("║   te presentarán opciones y decisiones a tomar. Lee               ║")
                print("║   cuidadosamente las descripciones y elige sabiamente, ya         ║")
                print("║   que tus elecciones afectarán el desarrollo de la historia       ║")
                print("║   y los desafíos que enfrentarás.                                 ║")
                print("╟───────────────────────────────────────────────────────────────────╢")
                print("║ 2. Combate: Cuando te encuentres en un enfrentamiento con un      ║")
                print("║    enemigo, tendrás la opción de atacar. Para ello,               ║")
                print("║    selecciona la opción de ataque y sigue las indicaciones        ║")
                print("║    para ejecutar tu movimiento. El daño infligido dependerá       ║")
                print("║    de tus atributos y de los del enemigo. ¡Derrota a tus          ║")
                print("║    enemigos para avanzar en tu aventura!                          ║")
                print("╟───────────────────────────────────────────────────────────────────╢")
                print("║ 3. Exploración: Durante el juego, podrás explorar diferentes      ║")
                print("║    ubicaciones. Examina cuidadosamente tu entorno y busca         ║")
                print("║    pistas, objetos valiosos y posibles peligros. Interactúa       ║")
                print("║    con los elementos y personajes que encuentres para             ║")
                print("║    descubrir secretos ocultos y desbloquear nuevas                ║")
                print("║    oportunidades.                                                 ║")
                print("╟───────────────────────────────────────────────────────────────────╢")
                print("║ 4. (SIN IMPLEMENTAR)                                              ║")
                print("║    Guardar y Cargar partida: Puedes guardar tu progreso en        ║")
                print("║    cualquier momento para continuar más tarde. Utiliza la         ║")
                print("║    opción de guardar partida y selecciona un espacio de           ║")
                print("║    guardado. Cuando desees continuar, selecciona la opción        ║")
                print("╚═══════════════════════════════════════════════════════════════════╝")
                
    
            elif opcion == "creditos" or opcion == "3": 
                print("╔══════════════════════════════════════════════════════════╗")
                print("║                    ¡Créditos del Juego!                  ║")
                print("║                                                          ║")
                print("║                 Autor: Juan Bautista Malina              ║")
                print("╚══════════════════════════════════════════════════════════╝")
                
        
            elif opcion == "salir" or opcion == "4":
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
                print("║                                                                                ║")
                print("║ ¡Gracias por jugar 'El Orbe de los Secretos'!                                  ║")
                print("║ Recuerda que siempre puedes regresar y sumergirte en esta fascinante travesía. ║")
                print("║ ¡Hasta la próxima! ¡Que tengas un día lleno de aventuras!                      ║")
                print("║                                                                                ║")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                break
        
            else: 
                print("Introduciste una opción no válida. Vuelve a Intentarlo...")
    
    


    @staticmethod 
    def frase_bienvenida():
        print("╔═════════════════════════════════════════════════════════════╗")
        print("║ ¡Bienvenido a 'El Orbe de los Secretos'!                    ║")
        print("║ Prepárate para embarcarte en una emocionante aventura       ║")
        print("║ llena de misterios y desafíos. En este mundo fascinante,    ║")
        print("║ te adentrarás en un viaje épico en busca de los secretos    ║")
        print("║ ocultos en antiguos orbes.                                  ║")
        print("║                                                             ║")
        print("║ Explora tierras desconocidas, resuelve enigmas intrigantes  ║")
        print("║ y enfréntate a peligrosas criaturas mientras te sumerges    ║")
        print("║ en una historia llena de magia y descubrimientos asombrosos.║")
        print("║                                                             ║")
        print("║ Conviértete en el valiente guerrero que desvelará los       ║")
        print("║ secretos más profundos y protegerá los misteriosos orbes    ║")
        print("║ de aquellos que desean utilizar su poder para fines oscuros.║")
        print("║                                                             ║")
        print("║ ¡Prepárate para una experiencia única llena de emociones,   ║")
        print("║ desafíos y sorpresas en 'El Orbe de los Secretos'! Que tus  ║")
        print("║ habilidades y valentía te guíen en esta gran aventura que   ║")
        print("║ está por comenzar. ¡Buena suerte, aventurero!               ║")
        print("╚═════════════════════════════════════════════════════════════╝")


