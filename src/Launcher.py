import math
import pygame
from src.Character import Character
class Launcher(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("assets/launcher.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image= pygame.transform.flip(self.image, False, True)
    self.image.set_colorkey((255,255,255))
    self.rect.x = x
    self.rect.y = y
    transColor = self.image.get_at((0,0))
    self.image.set_colorkey(transColor)
    self.up_direction = True
    self.vel= 2

  #update sprite position
  def update(self):
    #set sprite direction
    if self.rect.y == 0:
      self.up_direction = False
    if self.rect.y == 450:
      self.up_direction = True
    #sprite movement
    if self.up_direction == True:
      self.rect.y -= self.vel
    if self.up_direction == False:
      self.rect.y += self.vel

  #returns the position for new character
  def draw_new_character(self):
    return Character(self.rect.x, self.rect.y) 


    
  def launch_angle(self):
    mouse_x = 1 #get x value of mouse
    mouse_y = 1 
    self.angle = math.tan(mouse_y/mouse_x)
    #set launcher angle to angle and have it follow mouse movement
    pygame. transform. rotate(self.image, self.angle)
    