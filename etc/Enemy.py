class Enemy:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.health = 100
    self.alive = True
  def getX(self):
#	sets x cordinates value of enemy
#	args: int
#	return: returns integer and location of enemy
    return self.x
  def getY(self):
#	sets y cordinates value of enemy
#	args: int
#	return: returns integer and location of enemy
    return self.y

