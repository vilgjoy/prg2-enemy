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
    
    def check_death(self):
        print(f"kollar om du lever... du har {self.health} liv kvar.")
        if self.health <= 0:
            print("du är död, noob")
        else:
            print("du är inte död än")



gobo = Enemy(100, 10, "Gobo")
gobo.print_status()
slime = Enemy(100, 5, "Slimey")
slime.print_status()
while True:
    slime.attack(gobo)
    gobo.attack(slime)
    slime.check_death()
    gobo.check_death()
    if gobo.health <= 0 or slime.health <= 0:
        break
slime.check_death()
