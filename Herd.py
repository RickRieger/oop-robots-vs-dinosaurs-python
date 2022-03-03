from dinosaur import Dinosaur

class Herd:
  def __init__(self):
    self.dinosaurs = []

  def create_herd(self):
    tyrannosaurus_rex = Dinosaur('tyrannosaurus_rex', 30)
    stegosaurus = Dinosaur('stegosaurus', 30)
    velociraptor = Dinosaur('velociraptor', 30)
    self.dinosaurs = [tyrannosaurus_rex, stegosaurus, velociraptor]
    
      