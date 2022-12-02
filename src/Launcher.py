import pygame
from src.Character import Character

class Launcher(pygame.sprite.Sprite):
  def __init__(self, x, y):
    #sets up characteristics about launcher
    #input is self and x y coordinates
    #sets values
    super().__init__()
    self.image = pygame.image.load("assets/launcher.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image= pygame.transform.flip(self.image, False, True)
    self.image.set_colorkey((255,255,255))
    self.rect.x = x + 20
    self.rect.y = y - 40
    self.up_direction = True
    self.vel= 4
  #update sprite position
  def update(self):
    #set sprite direction and controls
    #only input is self
    #returns new y value of launcher
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_UP]:
      if self.rect.y > 100:
        self.rect.y -= self.vel
    if key_input[pygame.K_DOWN]:
      if self.rect.y < 410:
        self.rect.y += self.vel  
  def draw_new_character(self):
    #returns a Character using the position of the launcher
    #only argument is itself
    #returns current position of launcher and assigns those values to a newly created character
    return Character(self.rect.x + 50 , self.rect.y) 


    