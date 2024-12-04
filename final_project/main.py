import pygame
from src.controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()

main()