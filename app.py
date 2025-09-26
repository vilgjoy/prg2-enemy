class Enemy:
    def __init__(self, health: int, attack_power: int, name: str):
        self.health = health
        self.attack_power = attack_power
        self.name = name

    def print_status(self):
        print(f"{self.name} - hälsa: {self.health}, attack: {self.attack_power}")

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attackerar {target.name} för {self.attack_power} skada")
        if target.health <= 0:
            print(f"{self.name} har vunnit")
        else:
            pass


gobo = Enemy(30, 10, "Gobo")
gobo.print_status()
slime = Enemy(10, 5, "Slimey")
slime.print_status()
gobo.attack(slime)
gobo.print_status()
