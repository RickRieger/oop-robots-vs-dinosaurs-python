import time
import random

from fleet import Fleet
robots = fleet.robots

from herd import Herd
dinos = herd.dinosaurs

fleet = Fleet()
herd = Herd()

class Battlefield:
  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()  

  def run_game(self):
    self.display_welcome()
    players_choice = self.get_user_game_choice()
    fleet.create_fleet(players_choice)
    herd.create_herd(players_choice)
    self.battle(players_choice)
  
   
    
  def display_welcome(self):
    print('\n\nWELCOME TO DINOSAURS VS ROBOTS')
    print('==============================\n')

  def get_user_game_choice(self):
    print('In this game, you can choose to be Dinosaurs or Robots.\n')

    players_choice = input('Which will it be?\n\na. For Dinosaurs\nb. For Robots\n\nPlease provide your choice: ')

    return players_choice


  def print_dinos(self,dino_list):
    print('\nHere is your Dinosaur herd:\n')
    i = 0
    while i < len(dino_list):

      print(f'{i} for {dino_list[i].name}:\n   (health = {dino_list[i].health}  energy = {dino_list[i].energy}  attack_power = {dino_list[i].attack_power})')
      i += 1


  def battle(self, players_choice):

    print('===========BATTLE!===========\n')
    if players_choice == 'a':
      print('The fleet of Robots are approaching, time to make a move!')
    else: print('The herd of Dinosaurs are approaching, time to make a move!')
    if players_choice == 'a':
      self.print_dinos(herd.dinosaurs)
      dino_chosen = int(input('\nWhich Dinosaur would you like to attack with?: '))
      time.sleep(2) 
    while   
      self.dino_turn(dino_chosen)
         

  def get_random_player(self, list_of_team):
    index = random.randint(0,(len(list_of_team) - 1))
    return list_of_team[index]



  def dino_turn(self, dino_chosen):
    robot = self.get_random_player(fleet.robots)
    print(f'\n{herd.dinosaurs[dino_chosen].name} charges towards the robots and attacks {robot.name} with a {herd.dinosaurs[dino_chosen].attack_name}')
    time.sleep(2) 
    robot.health -= herd.dinosaurs[dino_chosen].attack_power
    print(f'\n{herd.dinosaurs[dino_chosen].name} delivers {herd.dinosaurs[dino_chosen].attack_power} pts of damage to {robot.name}')

    
      


  def robo_turn(self, robot_chosen):
    pass
  def show_dino_opponent_options(self):
    pass
  def show_robo_opponent_options(self):
    pass
  def display_winners(self):
    pass