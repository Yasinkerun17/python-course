from Enemy import *

class Zombie(Enemy):
    
    def __init__(self, health_points=10, attack_damage=1):
        super().__init__(type_of_enemy = "Zombie", health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("*Grumbling...*")