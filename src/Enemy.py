import pygame

class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
     super().__init__()
     self.image= pygame.image.load("assets/enemy.png").convert_alpha()
     self.rect = self.image.get_rect()
     self.image = pygame.transform.scale(self.image,(40,40))
     self.image.set_colorkey((255,255,255))
     self.rect = self.image.get_rect()
     self.rect.x = x
     self.rect.y = y
     self.vel = 5

     def update(self):
       self.rect.x += self.vel

    

    

  
  

