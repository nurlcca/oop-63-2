class Hero:
    #Class construction
    def __init__(self, nick, hp, lvl):
        #Class attributes
        self.nick = nick
        self.hero_hp = hp
        self.hero_lvl = lvl
    def action(self):
        return f"{self.nick} base action activate!"

#Child class
class MageHero(Hero):
    
    def __init__(self, nick, hp, lvl, mp):
        super().__init__(nick, hp, lvl)
        self.mp = mp

    def action(self):
        return f"This is new method for child class {self.nick}"

#asuna = Hero("Asuna", 999, 9999)
#mage_kirito = MageHero("Ardager", 100, 1000, 500)

#print(asuna.action())
#print(mage_kirito.action())

class Animal:
    def action(self):
        print(f"Animal action")

class Fly(Animal):
    def action(self):
        super().action()
        print(f"Fly action")

class Swim(Animal):
    def action(self):
        # super().action()
        print(f"Swin action")

class Duck(Fly,Swim):
    def action(self):
        super().action()
        print(f"Dunk action")

donald_duck = Duck()
donald_duck.action()
print(Duck.__mro__)