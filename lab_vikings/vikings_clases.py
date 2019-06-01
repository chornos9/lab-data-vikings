# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health -= damage
        
# Viking
class viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name


    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health >= 0:
            return self.name + "has received" + str(damage) + "points of damage"

        else:
            return self.name + "has died in the act of combat"

    def battleCry(self):
        return "Odín Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self.damage):
        super().receive_damage(damage)
        if self.health <= 0;
            return "A Saxon has died in combat"
        else 
            return "A Saxon has received" + str(damage) + "points of damage"


# War
class War:
    def __init__(self, viking_army=[], saxon_army=[])
        self.viking_army = viking_army
        self.saxon_army = saxon_army


    def add_viking(self, viking):
        self.viking_army.append(viking)

    def add_saxon(self, saxon_army):
        self.saxon_army += 1
        
    def viking_attack():
        self.saxon.receive_damage = viking.strength

    def saxon_attack():
        pass
    def show_status():
