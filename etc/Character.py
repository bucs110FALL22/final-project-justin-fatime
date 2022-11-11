class Character(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.damage = 60
    self.speed = 5 
  
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def moveLeft (self):
    if keyPressed("left"):
      self.x -=1
  def moveRight (self):
    if keyPressed("right"):
      self.x +=1
  def moveDown(self):
    if keyPressed("down"):
      self.y -=1
  def moveUp(self):
    if keyPressed("up"):
      self.y +=1 
