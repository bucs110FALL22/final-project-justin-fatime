import math
import pygame

class Launcher:
  def __init__(self, x, y):
    self.image =pygame.image.load("assets/slingshot.png").convert()
    self.rect = self.image.get_rect()
    self.image= pygame.transform.scale(self.image,(150,150))
    self.rect.x = x
    self.rect.y = y
    transColor = self.image.get_at((0,0))
    self.image.set_colorkey(transColor)
    #self.base_image = self.image = pygame.image.load("")
    #self._base_rect = self.image.get_rect()

  def launch_angle(self):
    mouse_x = 1 #get x value of mouse
    mouse_y = 1 
    self.angle = math.tan(mouse_y/mouse_x)
    #set launcher angle to angle and have it follow mouse movement
    pygame. transform. rotate(self.image, self.angle)
    