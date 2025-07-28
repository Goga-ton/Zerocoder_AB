from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец выбирает меч")
        print("Боец наносит удар мечом")
        print("Монстр побежден!")

class Bow(Weapon):
    def attack(self):
        print("Боец выбирает лук")
        print("Боец наносит удар луком")
        print("Монстр побежден!")

class Fighter:
    def __init__ (self, weapon):
        self.weapon = weapon

    def change_weapon(self):
        self.weapon.attack()

fightet1 = Fighter(Sword())
fightet1.change_weapon()

class Monster:
    pass