class Character(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.damage = 60
    self.speed = 5 
  
  def getX(self):
#	sets x cordinates value of character
#	args: int
#	return: returns integer and location of character
    return self.x
  def getY(self):
#	sets y cordinates value of character
#	args: int
#	return: returns integer and location of character
    return self.y
    
  def moveLeft (self):
#	moves character left 
#	args: self
#	return: moves characters position
    if keyPressed("left"):
      self.x -=1
  def moveRight (self):
#	moves character right 
#	args: self
#	return: moves characters position
    if keyPressed("right"):
      self.x +=1
  def moveDown(self):
#	moves character down 
#	args: self
#	return: moves characters position
    if keyPressed("down"):
      self.y -=1
  def moveUp(self):
#	moves character up 
#	args: self
#	return: moves characters position
    if keyPressed("up"):
      self.y +=1 
