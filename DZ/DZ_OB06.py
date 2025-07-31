class Hero:
    def __init__(self, name, healf=100, attack_power=20):
        self.name = name
        self.healf = healf
        self.attack_power = attack_power

    def attack(self, other: "Hero"):
        other.healf -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит урон {self.attack_power}.\n"
              f"У {other.name} осталось здоровья {other.healf}")

    def is_alives(self):
        return self.healf > 0

    def __str__(self):
        return (f"{self.name} (Здоровье: {self.healf}, Сила удара: {self.attack_power})")

class Game:
    def __init__(self, player1):
        self.player = Hero(player1)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начинаем игру:")
        print(f"Игрок: {self.player}")
        print(f"PC: {self.computer}")
        print("-" * 50)

        player_turn = 1 # 0 - игрок, 1 - компьютер

        while self.player.is_alives() and self.computer.is_alives():
            if player_turn == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            player_turn = 1 - player_turn
            print("-" * 50)

        if self.player.is_alives():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

play = Game("Антон")
play.start()


