import math
import pygame

class Block:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.image = self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.base_image = self.image = pygame.image.load("")
    self._base_rect = self.image.get_rect()

  def launch_angle(self):
    mouse_x = 1 #get x value of mouse
    mouse_y = 1 
    self.angle = math.tan(mouse_y/mouse_x)
    #set launcher angle to angle and have it follow mouse movement
    pygame. transform. rotate(self.image, self.angle)
    