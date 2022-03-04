from weapon import Weapon

class Robot:
  def __init__(self, name, weapon_name, attack_power):
    self.name = name
    self.health = 200
    self.power_level = 100
    self.weapon = Weapon(weapon_name, attack_power)

  def attack(self, dinosaur,):
    
    pass
      