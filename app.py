game_map = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

class Enemy:
    def __init__(self, health: int, attack_power: int, name: str, x: int, y: int):
        self.health = health
        self.attack_power = attack_power
        self.name = name
        self.x = x
        self.y = y

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
    
    def move(self, directionx, directiony, game_map):
        new_x = self.x + directionx
        new_y = self.y + directiony
        if (0 <= new_y < len(game_map)) and (0 <= new_x < len(game_map[0])) and (game_map[new_y][new_x] == 0):
            game_map[self.y][self.x] = 0
            game_map[new_y][new_x] = 1
            self.x = new_x
            self.y = new_y
            print(f"{self.name} flyttade till position ({self.x}, {self.y})")
        else:
            print(f"{self.name} kan inte flytta dit vro")


gobo = Enemy(100, 10, "Gobo", 0, 0)
gobo.move(1, 2, game_map)
gobo.move(1, 1, game_map)
