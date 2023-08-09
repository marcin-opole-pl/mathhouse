class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def get_damage(self, amount):
        self.health -= amount

class Scorpion(Monster):
    def __init__(self, health, energy, poison_damage):
        super().__init__(health, energy)
        self.poison_damage = poison_damage