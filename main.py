from src.Controller import Controller
import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    controller = Controller()
    #Call your mainloop
    controller.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
