import pygame
from Screens import Screens
import math

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    #set size of screem
    screen_demensions = [800,450]
    self.screen = pygame.display.set_mode(size=(screen_demensions[0],screen_demensions[1]))
    
  def mainloop(self):
    in_game = True
    in_pause = False
    playerSelection = 1
    
    in_menu = True
    #select state loop
    while in_game == True:
      if in_menu == True:
        selection = self.menuloop()  
        if selection == 1 or selection == 2 or selection == 3 or selection == 4:
          in_menu = False
          in_level = True     
      elif in_level == True:
        in_menu = self.gameloop(selection,in_pause)

      pygame.display.flip()
      
    
      
    
        
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    
      #event loop
    
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
      lvl_1_demensions = ((width/5)-(button_size/2),((height+100)/2)-(button_size/2),button_size,button_size)
      lvl_2_demensions = (((2*width)/5)-(button_size/2),((height+100)/2)-(button_size/2),button_size,button_size)
      lvl_3_demensions = (((3*width)/5)-(button_size/2),((height+100)/2)-(button_size/2),button_size,button_size)
      lvl_4_demensions = (((4*width)/5)-(button_size/2),((height+100)/2)-(button_size/2),button_size,button_size)
      lvl_1_select = pygame.Rect(lvl_1_demensions)
      lvl_2_select = pygame.Rect(lvl_2_demensions)
      lvl_3_select = pygame.Rect(lvl_3_demensions)
      lvl_4_select = pygame.Rect(lvl_4_demensions)
      exit_select = pygame.Rect(10,14,button_size/2,button_size/2)
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_click_pos = event.pos
          if lvl_1_select.collidepoint(mouse_click_pos):
            playerSelection = 1
            in_menu = False
            return playerSelection
          elif lvl_2_select.collidepoint(mouse_click_pos):
            playerSelection = 2
            in_menu = False
            return playerSelection
          elif lvl_3_select.collidepoint(mouse_click_pos):
            playerSelection = 3
            in_menu = False
            return playerSelection
          elif lvl_4_select.collidepoint(mouse_click_pos):
            playerSelection = 4
            in_menu = False
            return playerSelection
          elif exit_select.collidepoint(mouse_click_pos):
            pygame.quit()
      #redraw
      
      
  def gameloop(self,level,in_pause):
    
    #event loop
      size_list = pygame.display.get_window_size()
      game_level = level
      width = size_list[0]
      height = size_list[1]
      #Create an instance on your controller object
      controller = Screens()
      #Call your mainloop
      if in_pause == False:
        controller.update_game(self.screen,game_level)
        button_size = 50
        pause_select = pygame.Rect(10,10,button_size/2,button_size/2)
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if pause_select.collidepoint(mouse_click_pos):
              in_pause = True
      elif in_pause == True:
        controller.update_game(self.screen,game_level)
        controller.update_pause(self.screen,game_level)
        exit_select = pygame.Rect((width/2)-150,(height/2)-50,80,80)
        resume_select = pygame.Rect(((width/2)+18,(height/2)-50,80,80))
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if exit_select.collidepoint(mouse_click_pos):
              in_menu = True
              return in_menu
            elif resume_select.collidepoint(mouse_click_pos):
              in_pause = False

      #update data

      #redraw
      
  def gameoverloop(self):
      #event loop
    while gameover == True:
      pass

      #update data

      #redraw
      pygame.display.flip()
