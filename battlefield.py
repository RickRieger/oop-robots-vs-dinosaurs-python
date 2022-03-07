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
    herd.create_herd()
    self.battle(players_choice)
  
  def display_welcome(self):
    print('\n\nWELCOME TO DINOSAURS VS ROBOTS')
    print('==============================\n')

  def get_user_game_choice(self):
    print('In this game, you can choose to be Dinosaurs or Robots.\n')

    players_choice = input('Which will it be?\n\na. Dinosaurs\nb. Robots\n\nPlease provide your choice: ')

    print('\n\n')
    return players_choice


  def battle(self, players_choice):

    print('===========BATTLE!===========\n\n')
    if players_choice == 'a':
      print('The fleet of Robots are approaching, time to make a move!')
    else: print('The herd of Dinosaurs are approaching, time to make a move!')
    
    # User choses to play as Dinosaurs
    if players_choice == 'a':
      keep_battling = True
      while keep_battling:
        print('\n\nDINOSAURS ')
        print('=========')
        self.show_dino_opponent_options(herd.dinosaurs)
        dino_chosen = int(input('\nWhich Dinosaur would you like to attack with?: '))
        dino_chosen = herd.dinosaurs[dino_chosen]
        self.choose_dino_attack(dino_chosen)
        time.sleep(1) 
        self.dino_turn(dino_chosen, fleet.robots)
        # Break out of while loop if dino destroys robot
        if len(fleet.robots) == 0:
          break

        # Robot turn random selections
        random_robot = self.get_random_player(fleet.robots)
        time.sleep(1)
        print('===========THE ROBOTS STRIKE BACK!===========\n')
        time.sleep(1)
        self.robo_turn(random_robot, herd.dinosaurs)
        time.sleep(1)
        if len(fleet.robots) <= 0 or len(herd.dinosaurs) <= 0:
          keep_battling = False

    # User choses to play as Robots      
    elif players_choice == 'b':
      keep_battling = True
      while keep_battling:
        print('\n\nROBOTS ')
        print('=========')
        self.show_robo_opponent_options(fleet.robots)
        robot_chosen = int(input('\nWhich Robot would you like to attack with?: '))
        time.sleep(1)
        robot_chosen = fleet.robots[robot_chosen] 
        self.robo_turn(robot_chosen, herd.dinosaurs)
        # Break out of while loop if robot destroys dino
        if len(herd.dinosaurs) == 0:
          break

        # Dino turn random selections
        random_dino = self.get_random_player(herd.dinosaurs)
        time.sleep(1)
        print('===========THE DINOSAURS STRIKE BACK!===========\n')
        time.sleep(1)
        self.dino_turn(random_dino, fleet.robots)
        time.sleep(1)
        if len(herd.dinosaurs) <= 0 or len(fleet.robots) <= 0:
          keep_battling = False
    
    # Checks for winner of the game
    if len(herd.dinosaurs) > 0:
      winner = 'Dinosaurs' 
    else: winner = 'Robots'    
    self.display_winners(winner)       

  def get_random_player(self, list_of_team):
    if len(list_of_team) <= 1:
      return list_of_team[0]
    else:  
      index = random.randint(0,(len(list_of_team) - 1))
      return list_of_team[index]

  def dino_turn(self, dino_chosen, fleet_of_robots):
    robot = self.get_random_player(fleet.robots)
    dino_chosen.attack(robot, fleet_of_robots)

  def robo_turn(self, robot_chosen, herd_of_dinos):
    dino = self.get_random_player(herd.dinosaurs)
    robot_chosen.attack(dino, herd_of_dinos)

  def show_dino_opponent_options(self, dino_list):
    print('\nGo get them Robots!\n')
    i = 0
    while i < len(dino_list):
      print(f'{i} {dino_list[i].name}:\n   (health = {dino_list[i].health}  energy = {dino_list[i].energy}  attack_power = {dino_list[i].attack_power})\n')
      i += 1

  def choose_dino_attack(self, dino_chosen):
      print('\n\nATTACK MOVE ')
      print('===========\n')
      print(f'Please choose type of attack for {dino_chosen.name}:')
      
      attack_choice = int(input(f'\n1. {herd.attack_names[0]}\n2. {herd.attack_names[1]}\n3. {herd.attack_names[2]}\n\nYour answer: '))
      dino_chosen.attack_name = herd.attack_names[attack_choice - 1]

  def show_robo_opponent_options(self, robot_list):
      print('\nGo get them Dinosaurs!:\n')
      i = 0
      while i < len(robot_list):
        print(f'{i} {robot_list[i].name}:\n   (health = {robot_list[i].health}  power = {robot_list[i].power}  attack_power = {robot_list[i].weapon.attack_power})\n')
        i += 1

  def display_winners(self, winner):
    print(f'============================ The winner is {winner} ========================\n\n')
    if winner == 'Robots':
      print("After a long battle, the Dinosaurs just were'nt enough to beat the Robots.  Perhaps T_REX needs to step up the leadership a notch next time!")
    else: print("The Dinosaurs seemed to have crushed the Robots. What do you expect with a robot from the movie Space-Balls participating in the battle?") 

    print('\n\n\nThank you for playing!!!')