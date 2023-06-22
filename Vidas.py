"""
import time

class HealthBar:
    def __init__(self, total_health):
        self.total_health = total_health
        self.current_health = total_health

    def update(self, new_health):
        self.current_health = new_health

    def display(self):
        filled_cells = int((self.current_health / self.total_health) * 20)
        empty_cells = 20 - filled_cells

        bar = '█' * filled_cells + ' ' * empty_cells

        print(f'[{bar}]')

# Crear las barras de vida
player_health = HealthBar(100)
enemy_health = HealthBar(100)

# Ejemplo de actualización y visualización de las barras de vida
player_health.update(80)
enemy_health.update(60)

player_health.display()
enemy_health.display()

# Esperar un segundo antes de actualizar las barras de vida
time.sleep(1)

player_health.update(60)
enemy_health.update(20)

player_health.display()
enemy_health.display()
"""