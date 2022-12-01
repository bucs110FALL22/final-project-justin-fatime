import pygame

class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
     super().__init__()
     self.image= pygame.image.load("assets/enemy.png").convert_alpha()
     self.rect = self.image.get_rect()
     self.image = pygame.transform.scale(self.image,(40,40))
     self.image.set_colorkey((255,255,255))
     self.rect = self.image.get_rect(center= (x,y))
     self.rect.x = x
     self.rect.y = y
       
  def update(self):
      self.rect.x -= 4
      if self.rect.x == 0:
        self.kill()
      
        
        
   

    

    

  
  

