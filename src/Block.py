import pygame
class Block:
  def __init__(self, x, y):
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.rect.x= x
    self.rect.y= y
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

