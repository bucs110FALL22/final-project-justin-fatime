import pygame
import random
#import requests
#import io
#from urllib.request import urlopen
#req = requests.get(url= "https://random-d.uk/api/v2/random", headers={"User-Agent": "Mozilla/5.0"})
#print(req.status_code)
#duck = req.json()
#url = duck['url']
#image_url = url
#image_str = urlopen(image_url).read()
#image_file = io.BytesIO(image_str)
class Enemy(pygame.sprite.Sprite):
  def __init__(self, speed):
    #creates values for enemy class
    #only arguement is speed at which the enemies approach
    # sets values for enemies
     super().__init__()
     self.image=pygame.image.load("assets/enemy.png") #.convert_alpha()
     self.rect = self.image.get_rect()
     self.image = pygame.transform.scale(self.image,(40,40))
     self.rect = self.image.get_rect()
     self.rect.x = 800
     self.rect.y = random.randrange(100,400)
     self.speed = speed

  def update(self):
    #moves the enemies across the screen
    # no arguments besides self
    #changes the x position
    self.rect.x -= self.speed
    if self.rect.x == 0:
      self.speed = 0
      
  def position_x(self):
    #returns the position of object
    # only argument is self
    #returns x pos
    return self.rect.x
        
        
        
        
        
        

      
        
        
   

    

    

  
  

