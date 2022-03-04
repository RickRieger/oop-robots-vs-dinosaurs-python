from fleet import Fleet
from herd import Herd

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
    # print(herd.dinosaurs[0].name )
    
  def display_welcome(self):
    print('\n\nWELCOME TO DINOS VS BOTS')
    print('========================\n')

  def get_user_game_choice(self):
    print('In this game, you can choose to be dinosaurs or robots.\n')

    players_choice = input('Which would it be?\n\na. For dinosaurs\nb. For robots\n\nPlease provide your choice: ')

    return players_choice


  def battle(self):
    pass
  def dino_turn(self):
    pass
  def robo_turn(self):
    pass
  def show_dino_opponent_options(self):
    pass
  def show_robo_opponent_options(self):
    pass
  def display_winners(self):
    pass