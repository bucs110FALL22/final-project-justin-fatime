import pygame
import random

class Enemy(pygame.sprite.Sprite):
  def __init__(self, speed):
     super().__init__()
     self.image= pygame.image.load("assets/enemy.png").convert_alpha()
     self.rect = self.image.get_rect()
     self.image = pygame.transform.scale(self.image,(40,40))
     self.image.set_colorkey((255,255,255))
     self.rect = self.image.get_rect()
     self.rect.x = 800
     self.rect.y = random.randrange(100,400)
     self.speed = speed
     
  def update(self):
      self.rect.x -= self.speed
      if self.rect.x == 0:
        self.speed = 0
  def position_x(self):
    return self.rect.x
        
        
        
        
        
        

      
        
        
   

    

    

  
  

