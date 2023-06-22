"""import time
import sys

def pantalla_de_carga():
    print("Cargando...")
    barra = "[                    ]"
    for i in range(21):
        barra = barra[:i+1] + "█" + barra[i+2:]
        sys.stdout.write("\r" + barra + " " + str(i*5) + "%")
        sys.stdout.flush()
        time.sleep(0.1)  # Simula un retraso en la carga

    sys.stdout.write("\r" + barra + " 100%")
    sys.stdout.flush()
    print("\nCarga completa.")

pantalla_de_carga()"""