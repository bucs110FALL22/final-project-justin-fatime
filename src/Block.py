import pygame

class Block:
  def __init__(self, x, y):
    #block1
    self.image = pygame.image.load("assets/block1.png")
    self.image= pygame.transform.scale(self.image,(40,40))
    self.image.set_colorkey((255,255,255))
    self.rect = self.image.get_rect()
    self.rect.x= x
    self.rect.y= y
    self.w= self.image.get_width()
    self.h= self.image.get_height()
    #block2
    #self.image = pygame.image.load("assets/block2.png")
    #self.image= pygame.transform.scale(self.image,(40,40))
    #self.rect = self.image.get_rect()
    #self.rect.x= x
    #self.rect.y= y
    #block3
    #self.image = pygame.image.load("assets/block3.png")
    #block4
    #self.image = pygame.image.load("assets/block4.png")
    self.color = "brown"
    self.visible = True
    self.health = 10

  def destroyed(self):
#	makes destroyed block no longer visible
#	args: self
#	return: makes block invisible
    self.visible = False
    return self.visible

  def hitBlock(self):
#	takes health away from block when hit
#	args: self
#	return: lowers health
    self.health = self.health - 5
    return self.health

