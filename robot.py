from re import A
from weapon import Weapon
import time

class Robot:
  def __init__(self, name, weapon_name, attack_power):
    self.name = name
    self.health = 100
    self.power = 50
    self.weapon = Weapon(weapon_name, attack_power)

  def attack(self, dinosaur, herd_of_dinos):
    
    print(f'\n{self.name} charges towards the dinosaurs and attacks {dinosaur.name} with a {self.weapon.name}')

    time.sleep(1)

    dinosaur.health -= self.weapon.attack_power

    self.power -= 10

    if self.power <= 0:
      self.health -= 20
      self.power = 50

    elif dinosaur.health <= 0:
      print(f'\n\nZOINK!\n\nThey took out one of the dinosaurs! =====> It appears that {self.name} delivered a fatal blow to {dinosaur.name} with {self.weapon.name}\nThis delivered {self.weapon.attack_power} pts of damage, taking {dinosaur.name} out for good.\n(A trumpet in the distance playing taps...)\n\n')

      index = herd_of_dinos.index(dinosaur)
      herd_of_dinos.pop(index)  
      
    else: print(f'\n{self.name} delivers {self.weapon.attack_power} pts of damage to {dinosaur.name}\n\n')
   

      
