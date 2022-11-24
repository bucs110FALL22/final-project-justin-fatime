import math
import pygame

class Launcher:
  def __init__(self, x, y):
    self.image = pygame.image.load("assets/launcher.png")
    #.convert_alpha()
    self.image= pygame.transform.scale(self.image,(150,150))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    #self.image = pygame.Surface([640,480] ,pygame.SRCALPHA, 32)
    #self.image= self.image.convert_alpha()
    #self.base_image = self.image = pygame.image.load("")
    #self._base_rect = self.image.get_rect()

  def launch_angle(self):
    mouse_x = 1 #get x value of mouse
    mouse_y = 1 
    self.angle = math.tan(mouse_y/mouse_x)
    #set launcher angle to angle and have it follow mouse movement
    pygame. transform. rotate(self.image, self.angle)
    