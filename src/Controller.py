import pygame
from src.Screens import Screens

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
    #main loop of program that calls other loops into it. displays menu and buttons for different levels and to quit
    #
    #
    in_menu = True
      #event loop
    while in_menu == True:
      #Call your mainloop
      playerSelection = self.controller.update_menu(self.screen)
      if playerSelection != 0:
        self.gameloop(playerSelection)
      #redraw
      pygame.display.flip()
    return playerSelection
      
  def gameloop(self,level):
    #
    #
    #
    in_game = True
    in_pause = 'no'
    #event loop
    while in_game == True:
      #Call your mainloop
      if in_pause == 'no':
        in_pause = self.controller.update_game(self.screen,level)
      elif in_pause == 'yes':
        self.mainloop()
        #self.controller.update_pause(self.screen,level)
        #exit_select = pygame.Rect(250,175,80,80)
        #resume_select = pygame.Rect(418,175,80,80)
        #for event in pygame.event.get():
        #  if event.type == pygame.MOUSEBUTTONDOWN:
        #    mouse_click_pos = event.pos
        #    if exit_select.collidepoint(mouse_click_pos):
        #      self.mainloop()
        #    elif resume_select.collidepoint(mouse_click_pos):
        #      in_pause = False
      elif in_pause == 'lost':
        self.gameoverloop('lost')
          #self.gameoverLoop("lost")
      elif in_pause == 'won':
        self.gameoverloop('won')
          #self.gameoverLoop("won")
      #update data
      #redraw
      pygame.display.flip()

  def gameoverloop(self,game):
    #
    #
    #
    gameover = True
      #event loop
    while gameover == True:
      if game == "won":
        #show level complete screen and send back to menu
        pass
      else:
        #show back to menu or restart
        pass

      #update data

      #redraw
      pygame.display.flip()

  
