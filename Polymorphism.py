from Enemy import *
from Zombie import *
from Ogre import *

def battle(e: Enemy):
        e.talk()
        e.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 100)

battle(zombie)
zombie.talk()
zombie.attack()
# battle(ogre)
