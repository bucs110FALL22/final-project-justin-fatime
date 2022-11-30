import pygame
from src.Character import Character
from src.Launcher import Launcher
from src.Block import Block
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
    if level == 1:
      bg = pygame.image.load("assets/level1bg.png")
    elif level == 2:
      bg = pygame.image.load("assets/level2bg.png")
    elif level == 3:
      bg = pygame.image.load("assets/level3bg.png")
    elif level == 4:
      bg = pygame.image.load("assets/level4bg.png")
      
    screen.blit(bg,(0,0))
    #draw launcher
    #launcher = Launcher(0,270)
    #screen.blit(launcher.image, launcher.rect)
    #draw character 
    #sprite = Character(*screen.get_rect().center)
    #group = pygame.sprite.Group([
    #Character(screen.get_width() // 3, screen.get_height() // 3) 
  #])
    #sprite = Character(*screen.get_rect().center)
    #group = pygame.sprite.Group([Character(screen.get_width() // 3, screen.get_height() // 3)])
    
    #events = pygame.event.get()
    #clock = pygame.time.Clock()
    #clock.tick(60)
    #group.update(events)
    #screen.fill('light blue')
    #group.draw(screen)
    #pygame.display.flip()
    #draw blocks for level 1
    #if level==1:
        #block= Block(750,400)
        #screen.blit(block.image,block.rect)
       # block2= Block(730,400)
        #screen.blit(block2.image, block2.rect)
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