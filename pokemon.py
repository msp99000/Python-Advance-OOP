'''

Key Objectives
    - Create a Pokemon
    - View its details
    - Feed them to increase their health
    - Make them battle against each other and choose a winner

'''

class Pokemon:

    def __init__(self, name, level, health, attack, defense, speed):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

