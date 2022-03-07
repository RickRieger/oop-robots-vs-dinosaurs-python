import time
from fleet import Fleet
fleet = Fleet()

class Dinosaur:
  def __init__(self, name, attack_power, attack_name = ''):
      self.name = name
      self.attack_power = attack_power
      self.attack_name = attack_name
      self.health = 100
      self.energy = 50

  def attack(self, robot, fleet_of_robots):
    
    print(f'\n{self.name} charges towards the robots and attacks {robot.name} with a {self.attack_name}')

    time.sleep(1)

    robot.health -= self.attack_power

    self.energy -= 10

    if self.energy <= 0:
      self.health -= 20
      self.energy = 50

    elif robot.health <= 0:
      print(f'\n\nBAM! \nDESTRUCTION!\n\n=====> The {self.attack_name} that {self.name} gave {robot.name} proved to be just enough to take {robot.name} out of service. Say bye-bye to {robot.name}!\n\n')
      index = fleet_of_robots.index(robot)
      fleet_of_robots.pop(index)

    else: print(f'\n{self.name} delivers {self.attack_power} pts of damage to {robot.name}\n\n')

      

    
    
