import pygame

class Character(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("assets/bearcat.png")
    self.image= pygame.transform.scale(self.image,(40,40))
    self.image= pygame.transform.flip(self.image, True, False)
    self.rect = self.image.get_rect(center=(x,y))
    self.image.set_colorkey((255,255,255))
    self.dragging= False
    self.pos= (270,400)
  
  def update(self, events):
     for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.rect.collidepoint(event.pos)
                self.pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            if event.type == pygame.MOUSEMOTION and self.dragging:
                self.rect.topleft = event.pos[0] - self.pos[0], event.pos[1] - self.pos[1]
    
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

 
    
