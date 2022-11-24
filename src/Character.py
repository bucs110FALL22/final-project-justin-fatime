import pygame

class Character(pygame.sprite.Sprite):
  def __init__(self, x, y):
    #pygame.sprite.Sprite.__init__(self)
    super().__init__()
    self.image = pygame.image.load("assets/bearcat.png")
    self.rect = self.image.get_rect()
    self.rect.x= x
    self.rect.y= y
    self.image= pygame.transform.scale(self.image,(40,40))
    self.image= pygame.transform.flip(self.image, True, False)
    self.mass= 10
    self.damage = 60
  
  def update(self):
# update sprite position
    pass

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

  def launch(self, angle):
    pass
    #shoot birds out of cannon (launcher) with speed _ and be dragged down by gravity then collide with blocks and enemies

  def launch_speed(self):
    #speed and apex of air time depends on how far right on y axis mouse is
    #min speed =
    #max speed = 
    #show speed meter somewhere on screen
    
    #find a gravity library or extrapolate velocity y m and remove 9.8m per second
    #https://opensource.com/article/19/11/simulate-gravity-python
    
    #find collision library or way to make it when objects on screen hit they interact
    pass
    
