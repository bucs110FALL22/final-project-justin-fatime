import pygame
from Screens import Screens

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    #set size of screem
    screen_demensions = [800,450]
    self.screen = pygame.display.set_mode(size=(screen_demensions[0],screen_demensions[1]))
    
  def mainloop(self):
    #select state loop
    selection = self.menuloop()
    self.gameloop(selection)
  
  ### below are some sample loop states ###

  def menuloop(self):
    in_menu = True
    
      #event loop
    while in_menu == True:
      #Create an instance on your controller object
      controller = Screens()
      #Call your mainloop
      controller.update_menu(self.screen)
      #update data
      #create button locations and check if pressed
      button_size = 50
      size_list = pygame.display.get_window_size()
      width = size_list[0]
      height = size_list[1]
      lvl_1_demensions = ((width/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
      lvl_2_demensions = (((2*width)/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
      lvl_3_demensions = (((3*width)/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
      lvl_4_demensions = (((4*width)/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
      lvl_1_select = pygame.Rect(lvl_1_demensions)
      lvl_2_select = pygame.Rect(lvl_2_demensions)
      lvl_3_select = pygame.Rect(lvl_3_demensions)
      lvl_4_select = pygame.Rect(lvl_4_demensions)
      exit_select = pygame.Rect(10,10,button_size/2,button_size/2)
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_click_pos = event.pos
          if lvl_1_select.collidepoint(mouse_click_pos):
            playerSelection = 1
            in_menu = False
          elif lvl_2_select.collidepoint(mouse_click_pos):
            playerSelection = 2
            in_menu = False
          elif lvl_3_select.collidepoint(mouse_click_pos):
            playerSelection = 3
            in_menu = False
          elif lvl_4_select.collidepoint(mouse_click_pos):
            playerSelection = 4
            in_menu = False
          elif exit_select.collidepoint(mouse_click_pos):
            pygame.quit()
      #redraw
      pygame.display.flip()
    return playerSelection
      
  def gameloop(self,level):
    game_level = level
    in_game = True
    #event loop
    while in_game == True:
      #Create an instance on your controller object
      controller = Screens()
      #Call your mainloop
      controller.update_game(self.screen,game_level)
      button_size = 50
      exit_select = pygame.Rect(10,10,button_size/2,button_size/2)
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_click_pos = event.pos
          if exit_select.collidepoint(mouse_click_pos):
            in_game = False

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
