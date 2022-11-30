import pygame
from src.Screens import Screens
from src.Character import Character

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.display.init()
    #set size of screem
    screen_demensions = [800,450]
    self.screen = pygame.display.set_mode(size=(screen_demensions[0],screen_demensions[1]))
    self.controller = Screens()
    
  def mainloop(self):
    in_menu = True
      #event loop
    while in_menu == True:
      #Call your mainloop
      playerSelection = self.controller.update_menu(self.screen)
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
    in_game = True
    in_pause = False
    #event loop
    while in_game == True:
      #Call your mainloop
      if in_pause == False:
        in_pause = self.controller.update_game(self.screen,level)     
      elif in_pause == True:
        controller.update_game(self.screen,level)
        controller.update_pause(self.screen,level)
        exit_select = pygame.Rect(250,175,80,80)
        resume_select = pygame.Rect(418,175,80,80)
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if exit_select.collidepoint(mouse_click_pos):
              self.mainloop()
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

  
