import pygame
from src.Launcher import Launcher
from src.Enemy import Enemy
from os import path
HS_FILE = "highscore.txt"

class Screens():
  def __init__(self):
    self.load_data()
    
  def load_data(self):
    self.dir = path.dirname(__file__)
    with open(path.join(self.dir, HS_FILE), "r+") as f:
      try:
        self.highscore = int(f.read())
      except:
        self.highscore = 0
    
  def update_menu(self,screen):
    #sets background image of menu
    #arg: what screen to put image on
    #displays screen
    background = pygame.image.load("assets/mainScreenBackground.png")
    screen.blit(background, (0,0))
    
  def menuButtons(self):
    #create location and check if buttons in menu are clicked
    #only arg. is self
    #returns which button the player selected
    #update data
    #create button locations and check if pressed
    playerSelection = 0
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
    #creates the image of the game then creates image of characters on screen
    #args: self, which screen to do this on and which level is being played
    #returns state of game (in game, or won or lost)
    bg = pygame.image.load("assets/level"+ str(level)+"bg.png")  
    #creates sprites and sprite group 
    launcher_group = pygame.sprite.Group()
    launcher= Launcher(0,450)
    launcher_group.add(launcher)
    character_group = pygame.sprite.Group()
    if str(level) == "1":
      #creates 2 enemy sprites and sprite group for level 1
      enemy_group1= pygame.sprite.Group()
      for i in range(0,2):
      #sets enemy speed at 2
        enemy= Enemy(2)
        enemy_group1.add(enemy)
    if str(level) == "2":
      #creates 4 enemy sprites and sprite group for level 2
      enemy_group2= pygame.sprite.Group()
      for i in range(0,4):
      #sets enemy speed at 2
        enemy= Enemy(2)
        enemy_group2.add(enemy)
    if str(level) == "3":
      #creates 5 enemy sprites and sprite group for level 3
      enemy_group3= pygame.sprite.Group()
      for i in range(0,5):
      #sets enemy speed at 5
        enemy= Enemy(5)
        enemy_group3.add(enemy)
    if str(level) == "4":
      #creates 10 enemy sprites and sprite group for level 4
      enemy_group4= pygame.sprite.Group()
      for i in range(0,10):
      #sets enemy speed at 5
        enemy= Enemy(5)
        enemy_group4.add(enemy)
    
    #launcher + character movement
    #pause button
    in_pause = 'no'
    pause_select = pygame.Rect(10,10,25,25)   
    clock = pygame.time.Clock()
    
    #data = {'score': self.score} 
    #self.score = json.loads(open("assets/high_score.json").read())
    #starting score
    score = 100
    run = True
    while run:
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if pause_select.collidepoint(mouse_click_pos):
              in_pause = 'yes'
              run = False
        # draws a new character when spacebar is pressed
         key_input = pygame.key.get_pressed()   
         if key_input[pygame.K_SPACE]:
           character_group.add(launcher.draw_new_character())
         #creates a score event for every second that passes
         if level == 1:
           SCORE_EVENT = pygame.USEREVENT + 1
           pygame.time.set_timer(SCORE_EVENT, 1000)
           if event.type == SCORE_EVENT:
             score -= 10
            # return score
         #except:
            #pass
      #screen blit background every frame
      screen.blit(bg,(0,0))
      if level == 1:
        #pygame.event.get():
        #subtracts 5 points from total score every second
        #draw and update enemies on screen
        enemy_group1.draw(screen)
        enemy_group1.update()
        #check for collisions between character and enemy group
        pygame.sprite.groupcollide(character_group, enemy_group1, True, True)
        #check if won or lost
        if not enemy_group1:
          font = pygame.font.SysFont(None,24) 
          WHITE = ((255,255,255))
          #if the current user score is higher then their previous score then update highscore
          if score > self.highscore:
            self.highscore = score
          #display highscore on screen
          img1 = font.render('Highscore: ' + str(self.highscore), True, (WHITE))
          screen.blit(img1,(225,350))
          in_pause = 'won'
          run = False
        for i in enemy_group1:
          #check if enemy made it past character and if so the game is lost
          if i.position_x() == 20:
            in_pause = 'lost'
            run = False
      elif level == 2:
        #draw and update enemies on screen
        enemy_group2.draw(screen)
        enemy_group2.update()
        #check for collisions between character and enemy group
        pygame.sprite.groupcollide(character_group, enemy_group2, True, True)
        
        #check if won
        if not enemy_group2:
         in_pause = 'won'
         run = False
        for i in enemy_group2:
          if i.position_x() == 20:
            in_pause = 'lost'
            run = False
        
      elif level == 3:
        #draw and update enemies on screen
        enemy_group3.draw(screen)
        enemy_group3.update()
        #check for collisions between character and enemy group
        pygame.sprite.groupcollide(character_group, enemy_group3, True, True)
        #check if won
        if not enemy_group3:
         in_pause = 'won'
         run = False
        for i in enemy_group3:
          if i.position_x() == 20:
            in_pause = 'lost'
            run = False
          
      elif level == 4:
        #draw and update enemies on screen
        enemy_group4.draw(screen)
        enemy_group4.update()
        pygame.sprite.groupcollide(character_group, enemy_group4, True, True)
        #check if won
        if not enemy_group4:
         in_pause = 'won'
         run = False
        for i in enemy_group4:
          if i.position_x() == 20:
            in_pause = 'lost'
            run = False
         
      character_group.draw(screen)
      launcher_group.draw(screen)
      character_group.update()
      launcher_group.update()
      pygame.display.flip()
      #set frame rate for game
      clock.tick(60)
    return in_pause
    
  def game_won(self,screen,level):
    #if the level is completed show pop up for completed
    #arg: self, which screen to blit onto and what level
    #displays on screen
    pause = pygame.image.load("assets/levelCompleted.png")
    screen.blit(pause,(225,100))
    
  def game_lost(self,screen,level):
     #if the level is failed show pop up for lost
    #arg: self, which screen to blit onto and what level
    #displays on screen
      pause = pygame.image.load("assets/loseScreen.png")
      screen.blit(pause,(225,100))
      