import pygame
import os

class StatusBar():
    def __init__(self, x, y, w, h, max_value, label, depletion_rate):
        """
        Initializes the StatusBar object
        Args:
            x (int): x-coordinate
            y (int): y-coordinate
            w (int): width
            h (int): height
            max_value (int): max value of status bar
            label (str): title of status bar
            depletion_rate (int): rate of depletion
        Returns: None
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.value = max_value
        self.max_value = max_value
        self.label = label
        self.depletion_rate = depletion_rate
        
    def update(self, delta_time):
        """
        Updates status bar to deplete with time
        Args:
            delta_time (int): time
        Returns: None
        """
        self.value -= self.depletion_rate * delta_time
        if self.value < 0:
            self.value = 0
               
    def draw(self, screen):
        """
        Draws status bars
        Args:
            screen (display): status bar screen
        Returns: None
        """
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.w, self.h))
        
        ratio = self.value / self.max_value
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.w * ratio, self.h))
        
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        font = pygame.font.Font(font_path, 10)
        label_text = font.render(self.label, True, (255, 255, 255))
        screen.blit(label_text, (self.x, self.y - 15))