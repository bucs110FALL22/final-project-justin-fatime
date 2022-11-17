import pygame

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    #set size of screem
    width = 800
    height = 450
    self.screen = pygame.display.set_mode(width,height)
    
  def mainloop(self):
    #select state loop
    self.menuloop()
  
  ### below are some sample loop states ###

  def menuloop(self):
    in_menu = True
    
      #event loop
    while in_menu == True:
      pass
    

      #update data

      #redraw
      pygame.display.flip()
      
  def gameloop(self):
      #event loop
    while in_game == True:
      pass

      #update data

      #redraw
      pygame.display.flip()
  def gameoverloop(self):
      #event loop
    while gameover == True:
      pass

      #update data

      #redraw
      pygame.display.flip()
