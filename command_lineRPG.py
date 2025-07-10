class Character: 
    def __init__(self, name, health, attack_power):
        self.name = name 
        self.health = health 
        self.attack_power = attack_power
        self.inventory = []
    def take_damage(self, amount):
        self.health-= amount 
        print(f"{self.name} takes {amount} damage. Health is now {self.health}")
    def attack(self, enemy): 
        enemy.take_damage(self.attack_power)
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")
    def is_alive(self):
        if self.health > 0: 
            return True 
        else: 
            return False
class Enemy(Character):
    def __init__(self, enemy_type): 
        super().__init__("Goblin", 50, 5)
        if enemy_type == "Goblin": 
            name = "Goblin"
            health = 50
            attack_power = 5
        elif enemy_type == "Orc": 
            name = "Orc"
            health = 40
            attack_power = 10
        super().__init__(name, health, attack_power)