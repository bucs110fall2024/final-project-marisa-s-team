import pygame
from src.controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()

    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
main()