from weapon import Weapon
import time

class Robot:
  def __init__(self, name, weapon_name, attack_power):
    self.name = name
    self.health = 30
    self.power = 50
    self.weapon = Weapon(name, attack_power)

  def attack(self, dinosaur, herd_of_dinos):
    
    print(f'\n{self.name} charges towards the dinosaurs and attacks {dinosaur.name} with a {self.weapon.name}')

    time.sleep(1)

    dinosaur.health -= self.weapon.attack_power

    self.power -= 10

    if self.power <= 0:
      self.health -= 20
      self.power = 50

    elif dinosaur.health <= 0:
      print(f'\n\nBAM! They took out one of the dinosaurs! =====> It appears that {self.name} delivered a fatal blow to {dinosaur.name} with {self.weapon.name}, delivering {self.weapon.attack_power} pts of damage, taking {dinosaur.name} out for good. (A trumpet in the distance playing taps...)')

      index = herd_of_dinos.index(dinosaur)
      herd_of_dinos.pop(index)  

    print(f'\n{self.name} delivers {self.weapon.attack_power} pts of damage to {dinosaur.name}\n\n')
      