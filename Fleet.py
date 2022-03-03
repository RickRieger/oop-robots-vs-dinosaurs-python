from robot import Robot

class Fleet:
  def __init__(self):
    self.robots = []
      
  def create_fleet(self):
    johnny_5 = Robot('johnny_5', 50)    
    dot_matrix = Robot('dot_matrix', 50)    
    ed_209 = Robot('ed_209', 50)  
    self.robots = [johnny_5, dot_matrix, ed_209]