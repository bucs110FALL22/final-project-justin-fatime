import pygame

class Screens():
  def __init__(self):
    pass

  def update_menu(self,screen):
    size_list = pygame.display.get_window_size()
    width = size_list[0]
    height = size_list[1]
    screen.fill('light green')
    button_size = 50
    #draw level buttons
    lvl_1_demensions = ((width/5)-(button_size),((height+100)/2)-(button_size/2),button_size,button_size)
    lvl_2_demensions = (((2*width)/5)-(button_size),((height+100)/2)-(button_size/2),button_size,button_size)
    lvl_3_demensions = (((3*width)/5)-(button_size),((height+100)/2)-(button_size/2),button_size,button_size)
    lvl_4_demensions = (((4*width)/5)-(button_size),((height+100)/2)-(button_size/2),button_size,button_size)
    pygame.draw.rect(screen,'brown',(lvl_1_demensions))
    pygame.draw.rect(screen,'brown',(lvl_2_demensions))
    pygame.draw.rect(screen,'brown',(lvl_3_demensions))
    pygame.draw.rect(screen,'brown',(lvl_4_demensions))
    #write x for escape button
    font_x = pygame.font.Font(None, 70)
    font_object = font_x.render('x', True, "black")
    screen.blit(font_object, (10,1))
    #draw title
    msg = 'Angry Bearcats'
    font = pygame.font.Font(None, 70)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, (width/2-250, 40))
    #draw level title
    msg = 'levels:'
    font = pygame.font.Font(None, 50)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, (width/2-100, 180))
    #draw level numbers
    msg = '1'
    font = pygame.font.Font(None, 60)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, ((width/5)-36,((height+110)/2)-(button_size/2)))
    msg = '2'
    font = pygame.font.Font(None, 60)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, (((2*width)/5)-36,((height+110)/2)-(button_size/2)))
    msg = '3'
    font = pygame.font.Font(None, 60)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, (((3*width)/5)-36,((height+110)/2)-(button_size/2)))
    msg = '4'
    font = pygame.font.Font(None, 60)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, (((4*width)/5)-36,((height+110)/2)-(button_size/2)))

  def update_game(self,screen,level):
    size_list = pygame.display.get_window_size()
    button_size = 50
    width = size_list[0]
    height = size_list[1]
    background = 'light blue'
    screen.fill(background)
    #draw escape button
    #draw title
    msg = 'Level ' + str(level)
    font = pygame.font.Font(None, 70)
    font_object = font.render(msg, True, "white")
    screen.blit(font_object, (width/2-110, 40))
    #pause button
    pygame.draw.rect(screen,'black',(10,10,button_size/2,button_size/2))
    pygame.draw.rect(screen,background,(18.33,10,button_size/6,button_size/2))
