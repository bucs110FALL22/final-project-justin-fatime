import pygame
from src.Launcher import Launcher

class Screens():
  def __init__(self):
    pass

  def update_menu(self,screen):
    playerSelection = 0
    background = pygame.image.load("assets/mainScreenBackground.png")
    screen.blit(background, (0,0))
    #update data
    #create button locations and check if pressed
    lvl_1_select = pygame.Rect(135,250,50,50)
    lvl_2_select = pygame.Rect(295,250,50,50)
    lvl_3_select = pygame.Rect(455,250,50,50)
    lvl_4_select = pygame.Rect(615,250,50,50)
    exit_select = pygame.Rect(10,14,25,25)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_click_pos = event.pos
          if lvl_1_select.collidepoint(mouse_click_pos):
            playerSelection = 1
          elif lvl_2_select.collidepoint(mouse_click_pos):
            playerSelection = 2
          elif lvl_3_select.collidepoint(mouse_click_pos):
            playerSelection = 3
          elif lvl_4_select.collidepoint(mouse_click_pos):
            playerSelection = 4
          elif exit_select.collidepoint(mouse_click_pos):
            pygame.quit()
    return playerSelection

  def update_game(self,screen,level):
    bg = pygame.image.load("assets/level"+ str(level)+"bg.png")
    #if level == 1:
     # bg = pygame.image.load("assets/level1bg.png")
  #  elif level == 2:
   #   bg = pygame.image.load("assets/level2bg.png")
   # elif level == 3:
   #   bg = pygame.image.load("assets/level3bg.png")
   # elif level == 4:
   #   bg = pygame.image.load("assets/level4bg.png")
      
    screen.blit(bg,(0,0))
    
    #creates sprites and sprite group 
    launcher_group = pygame.sprite.Group()
    launcher= Launcher(0,450)
    launcher_group.add(launcher)
    character_group = pygame.sprite.Group()
    clock = pygame.time.Clock()
    #launcher + character movement
    run = True
    while run:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
          run = False
        # draws a new character when mouse lciked 
         if event.type == pygame.MOUSEBUTTONDOWN:
          character_group.add(launcher.draw_new_character())
      screen.blit(bg,(0,0))
      character_group.draw(screen)
      launcher_group.draw(screen)
      character_group.update()
      launcher_group.update()
      pygame.display.flip()
      clock.tick(60)
    pygame.quit()
    exit()
    #pause button
    in_pause = False
    pause_select = pygame.Rect(10,10,25,25)
    for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if pause_select.collidepoint(mouse_click_pos):
              in_pause = True
    return in_pause
    
  def update_pause(self,screen,level):
    pause = pygame.image.load("assets/pause.png")
    screen.blit(pause,(225,100))