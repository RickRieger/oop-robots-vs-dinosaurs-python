from fleet import Fleet
from herd import Herd
class Battlefield:
  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()  

  def run_game(self):
    self.display_welcome()
    Fleet.create_fleet(self)
    Herd.create_herd(self)

  def display_welcome(self):
    print('WELCOME TO DINOS VS BOTS')
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