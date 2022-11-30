import pygame
from src.Launcher import Launcher
#from src.Enemy import Enemy
#import random

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
    #creates sprites and sprite group 
    launcher_group = pygame.sprite.Group()
    launcher= Launcher(0,450)
    launcher_group.add(launcher)
    character_group = pygame.sprite.Group()
    #enemy_group = pygame.sprite.Group()
    #enemy_group = Enemy(800,random.randrange(0,450))
    
    clock = pygame.time.Clock()
    #launcher + character movement
    #pause button
    in_pause = False
    pause_select = pygame.Rect(10,10,25,25)   
    run = True
    while run:
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if pause_select.collidepoint(mouse_click_pos):
              in_pause = True
              run = False
        # draws a new character when mouse clicked 
         key_input = pygame.key.get_pressed()   
         if key_input[pygame.K_SPACE]:
           character_group.add(launcher.draw_new_character())
           
      screen.blit(bg,(0,0))
      character_group.draw(screen)
      launcher_group.draw(screen)
      #enemy_group.draw(screen)
      character_group.update()
      launcher_group.update()
      #if level == 1:
         # enemy_group= pygame.sprite.Group()
          #enemy1= Enemy(600,100)
          #enemy2= Enemy(600,250)
          #enemy3 = Enemy(600,400)
          #enemy4 = Enemy(400,150)
          #enemy5 = Enemy(400,300)
          #enemy_group.add(enemy1, enemy2, enemy3, enemy4, enemy5)
          #enemy_group.draw(screen)
      #pygame.sprite.groupcollide(character_group, enemy_group, True, True)
      pygame.display.flip()
      clock.tick(60)
    return in_pause
    
  def update_pause(self,screen,level):
    pause = pygame.image.load("assets/pause.png")
    screen.blit(pause,(225,100))