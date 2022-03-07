from robot import Robot

class Fleet:
  def __init__(self):
    self.robots = []
    self.weapons = ['A LASER BEAM', 'A METAL PURSE', 'GATLING GUNS']  

  def create_fleet(self, players_choice):
    
    if players_choice == 'a':
          johnny_5 = Robot(f'JOHNNY_5', self.weapons[0], 30)
          dot_matrix = Robot(f'DOT_MATRIX', self.weapons[1], 10)
          ed_209 = Robot(f'ED_209', self.weapons[2], 60)
    else:  
      print('\n\nROBOTS ')
      print('======\n')
      print('\nPlease choose a weapon for johnny_5:')

      weapon_choice = int(input(f'\n1. {self.weapons[0]}\n2. {self.weapons[1]}\n3. {self.weapons[2]}\n\nYour answer: '))
      johnny_5 = Robot(f'johnny_5', self.weapons[weapon_choice - 1], 30)
      self.weapons.remove(self.weapons[weapon_choice - 1])

      print('\nPlease choose a weapon for dot_matrix:')

      weapon_choice = int(input(f'1. {self.weapons[0]}\n2. {self.weapons[1]}\nYour answer: '))
      dot_matrix = Robot(f'dot_matrix', self.weapons[weapon_choice - 1], 10)
      self.weapons.remove(self.weapons[weapon_choice - 1])

      print(f'\ned_209 will be assigned this weapon by default ===> {self.weapons[0]}\n\n')

      ed_209 = Robot(f'ed_209', {self.weapons[0]}, 60)

    self.robots = [johnny_5, dot_matrix, ed_209]
  
