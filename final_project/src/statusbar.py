import pygame
import os

# Constants
END_STATS = 0
DEPLETION_STAT_BAR_COLOR = (255, 0, 0)
FULL_STAT_BAR_COLOR = (0, 255, 0)
STAT_BAR_LABEL_COLOR = (255, 255, 255)

class StatusBar():
    """
    StatusBar classs which creates and updates the three status bars (health, hunger, and happiness)
    """
    def __init__(self, x, y, w, h, max_value, label, depletion_rate):
        """
        Initializes the StatusBar object
        Args:
            x (int): The x-coordinate of the status bar
            y (int): The y-coordinate of the status bar
            w (int): The width of the status bar
            h (int): The height of the status bar
            max_value (int): The maximum value of the status bar
            label (str): The label of the status bar
            depletion_rate (float): The rate of depletion of the status bar
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
            delta_time (int): The time passed since the last update
        Returns: None
        """
        if self.value > END_STATS:
            self.value -= self.depletion_rate * delta_time / 1000
            if self.value < END_STATS:
                self.value = END_STATS
               
    def draw(self, screen):
        """
        Draws status bars
        Args:
            screen (pygame.Surface): The surface to draw status bars
        Returns: None
        """
        pygame.draw.rect(screen, (DEPLETION_STAT_BAR_COLOR), (self.x, self.y, self.w, self.h))
        
        fill_width = (self.value / self.max_value) * self.w
        pygame.draw.rect(screen, (FULL_STAT_BAR_COLOR), (self.x, self.y, fill_width, self.h))
        
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        font = pygame.font.Font(font_path, 10)
        label_text = font.render(self.label, True, (STAT_BAR_LABEL_COLOR))
        screen.blit(label_text, (self.x, self.y - 15))
        
        # UPDATE