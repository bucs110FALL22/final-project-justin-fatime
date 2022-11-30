import pygame

class Character(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("assets/bearcat.png").convert_alpha()
    self.image= pygame.transform.scale(self.image,(40,40))
    self.image= pygame.transform.flip(self.image, True, False)
    self.rect = self.image.get_rect(center=(x,y))
    self.image.set_colorkey((255,255,255))
    self.vel = 2

  def update(self):
    # updates character x values
    self.rect.x += 5
    #kill character if goes off screen 
    screen_width= 800
    if self.rect.x >= screen_width + 100:
      self.kill()



    

    

    
  

  

 
    
