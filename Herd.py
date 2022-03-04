from re import A
from dinosaur import Dinosaur

class Herd:
  def __init__(self):
    self.dinosaurs = []
    self.attack_names = ['bite', 'tail whip', 'crush']

  def create_herd(self, players_choice):
    if players_choice == 'b':
      t_rex = Dinosaur('t_rex', 40)
      stegosaurus = Dinosaur('stegosaurus', 25)
      velociraptor = Dinosaur('velociraptor', 35)
    else:
      print('\n\nDINOSAURS ')
      print('=========\n')
      print('Please choose an attack for t_rex:')
      
      attack_choice = int(input(f'\n1. {self.attack_names[0]}\n2. {self.attack_names[1]}\n3. {self.attack_names[2]}\n\nYour answer: '))
      t_rex = Dinosaur(f't_rex', 30, self.attack_names[attack_choice - 1])
      self.attack_names.remove(self.attack_names[attack_choice - 1])

      print('\nPlease choose an attack for stegosaurus:')

      attack_choice = int(input(f'\n1. {self.attack_names[0]}\n2. {self.attack_names[1]}\n\nYour answer: '))
      stegosaurus = Dinosaur(f'stegosaurus', 10, self.attack_names[attack_choice - 1])
      self.attack_names.remove(self.attack_names[attack_choice - 1])

      print(f'\nvelociraptor will be assigned this attack by default ===> {self.attack_names[0]}\n\n')

      velociraptor = Dinosaur(f'velociraptor', 60, {self.attack_names[0]})

    self.dinosaurs = [t_rex, stegosaurus, velociraptor]
  
    
    