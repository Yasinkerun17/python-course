from Enemy import *
from Zombie import *
from Ogre import *
zombie = Zombie(10, 1)
ogre = Ogre(20,10)

print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and attact damage is {zombie.attack_damage}")
print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and attact damage is {ogre.attack_damage}")
print(zombie.talk())
print(ogre.talk())

print(ogre.walk_forward())
