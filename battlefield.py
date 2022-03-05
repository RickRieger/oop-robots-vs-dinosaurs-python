import time
import random

from fleet import Fleet
fleet = Fleet()

from herd import Herd
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

    players_choice = input('Which will it be?\n\na. Dinosaurs\nb. Robots\n\nPlease provide your choice: ')

    return players_choice


  def print_dinos(self,dino_list):
      pass


  def battle(self, players_choice):

    print('===========BATTLE!===========\n\n')
    if players_choice == 'a':
      print('The fleet of Robots are approaching, time to make a move!')
    else: print('The herd of Dinosaurs are approaching, time to make a move!')
    
    if players_choice == 'a':
      keep_battling = True
      while keep_battling:
        print('\nHere is your Dinosaur herd:\n')
        self.show_dino_opponent_options(herd.dinosaurs)
        dino_chosen = int(input('\nWhich Dinosaur would you like to attack with?: '))
        time.sleep(1) 
        self.dino_turn(dino_chosen, fleet.robots)
        random_robot = self.get_random_player(fleet.robots)
        time.sleep(1)
        print('===========THE ROBOTS STRIKE BACK!===========\n')
        time.sleep(1)
        self.robo_turn(random_robot, herd.dinosaurs)
        time.sleep(1)
        if len(fleet.robots) <= 0 or len(herd.dinosaurs) <= 0:
          keep_battling = False

    if len(herd.dinosaurs) > 0:
      winner = 'Dinosaurs' 
    else: winner = 'Robots'    
    self.display_winners(winner)       

  def get_random_player(self, list_of_team):
    if len(list_of_team) == 1:
      return list_of_team[0]
    else:  
      index = random.randint(0,(len(list_of_team) - 1))
      return list_of_team[index]


  def dino_turn(self, dino_chosen, fleet_of_robots):
    robot = self.get_random_player(fleet.robots)
    herd.dinosaurs[dino_chosen].attack(robot, fleet_of_robots)


  def robo_turn(self, robot_chosen, herd_of_dinos):
    dino = self.get_random_player(herd.dinosaurs)
    robot_chosen.attack(dino, herd_of_dinos)

  def show_dino_opponent_options(self, dino_list):
    print('\nGo get them Robots!:\n')
    i = 0
    while i < len(dino_list):
      print(f'{i} {dino_list[i].name}:\n   (health = {dino_list[i].health}  energy = {dino_list[i].energy}  attack_power = {dino_list[i].attack_power})\n')
      i += 1




  def show_robo_opponent_options(self):
    pass
  def display_winners(self, winner):
    print(f'=============================The winner is {winner}=========================')