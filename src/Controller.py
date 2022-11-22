import pygame
from src.Screens import Screens

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    #set size of screem
    screen_demensions = [800,450]
    self.screen = pygame.display.set_mode(size=(screen_demensions[0],screen_demensions[1]))
    
  def mainloop(self):
    in_menu = True
      #event loop
    while in_menu == True:
      #Create an instance on your controller object
      controller = Screens()
      #Call your mainloop
      playerSelection = controller.update_menu(self.screen)
      if playerSelection == 1:
        self.gameloop(playerSelection)
      elif playerSelection == 2:
        self.gameloop(playerSelection)
      elif playerSelection == 3:
        self.gameloop(playerSelection)
      elif playerSelection == 4:
        self.gameloop(playerSelection)
      #redraw
      pygame.display.flip()
    return playerSelection
      
  def gameloop(self,level):
    game_level = level
    in_game = True
    in_pause = False
    size_list = pygame.display.get_window_size()
    width = size_list[0]
    height = size_list[1]
    #event loop
    while in_game == True:
      #Create an instance on your controller object
      controller = Screens()
      #Call your mainloop
      if in_pause == False:
        in_pause = controller.update_game(self.screen,game_level)
        
      elif in_pause == True:
        controller.update_game(self.screen,game_level)
        controller.update_pause(self.screen,game_level)
        exit_select = pygame.Rect((width/2)-150,(height/2)-50,80,80)
        resume_select = pygame.Rect(((width/2)+18,(height/2)-50,80,80))
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if exit_select.collidepoint(mouse_click_pos):
              self.menuloop()
            elif resume_select.collidepoint(mouse_click_pos):
              in_pause = False
      #update data
      #redraw
      pygame.display.flip()
      
  def gameoverloop(self):
    gameover = False
      #event loop
    while gameover == True:
      pass

      #update data

      #redraw
      pygame.display.flip()
