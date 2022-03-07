from dinosaur import Dinosaur

class Herd:
  def __init__(self):

    self.dinosaurs = []
    self.attack_names = ['CRUSHING BITE', 'THRASHING TAIL WHIP', 'FORCEFUL FOOT STOMP']

  def create_herd(self):
    
    t_rex = Dinosaur('T_REX', 40)
    stegosaurus = Dinosaur('STEGOSAURUS', 25)
    velociraptor = Dinosaur('VELOCIRAPTOR', 35)

    self.dinosaurs = [t_rex, stegosaurus, velociraptor]
  
    
    