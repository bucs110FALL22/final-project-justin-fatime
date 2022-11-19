import pygame

class Menu():
  def __init__(self):
    pass

  def update_menu(self):
    size_list = pygame.display.get_window_size()
    width = size_list[0]
    height = size_list[1]
    self.fill('light green')
    button_size = 50
    #draw level buttons
    lvl_1_demensions = ((width/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
    lvl_2_demensions = (((2*width)/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
    lvl_3_demensions = (((3*width)/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
    lvl_4_demensions = (((4*width)/5)-(button_size/2),(height/2)-(button_size/2),button_size,button_size)
    pygame.draw.rect(self,'brown',(lvl_1_demensions))
    pygame.draw.rect(self,'brown',(lvl_2_demensions))
    pygame.draw.rect(self,'brown',(lvl_3_demensions))
    pygame.draw.rect(self,'brown',(lvl_4_demensions))
    #draw escape button
    pygame.draw.rect(self,'black',(10,10,button_size/2,button_size/2))
    #draw title
    #asking player for input
    msg = 'Angry Bearcats'
    font = pygame.font.Font(None, 30)
    font_object = font.render(msg, True, "white")
    self.blit(font_object, (width/2, 40))

    #create button locations and check if pressed
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
            selection = True
          elif lvl_2_select.collidepoint(mouse_click_pos):
            playerSelection = 2
            selection = True
          elif lvl_3_select.collidepoint(mouse_click_pos):
            playerSelection = 3
            selection = True
          elif lvl_4_select.collidepoint(mouse_click_pos):
            playerSelection = 4
            selection = True
          elif exit_select.collidepoint(mouse_click_pos):
            pygame.quit()
