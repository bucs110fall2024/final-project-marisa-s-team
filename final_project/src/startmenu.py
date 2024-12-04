import pygame
import os

# Constants
ALL_RECTANGLES_HEIGHT = 50
START_MENU_TEXT_COLOR = (255, 255, 255)
START_BUTTON_COLOR = (155, 222, 140)
NAME_RECTANGLE_COLOR = (255, 255, 255)
CAT_BUTTON_COLOR = (219, 128, 64)
DOG_BUTTON_COLOR = (97, 64, 42)
BUTTON_HOVER_COLOR = (245, 147, 238)

class StartMenu:
    """
    StartMenu class which displays the start menu and allows user to interact with it
    """
    def __init__(self, screen, font):
        """
        Initializes StartMenu object
        Args:
            screen (pygame.Surface): The start menu display
            font (pygame.font.Font): The font of the start menu text
        Returns: None
        """
        self.screen = screen
        self.font = font
        self.pet_name = ''
        self.selected_pet = None
        self.is_active = True
        
        # Interactive elements
        self.start_button = pygame.Rect(300, 300, 200, ALL_RECTANGLES_HEIGHT)
        self.input_box = pygame.Rect(250, 200, 300, ALL_RECTANGLES_HEIGHT)
        self.active_input = False
        self.cat_button = pygame.Rect(150, 300, 100, ALL_RECTANGLES_HEIGHT)
        self.dog_button = pygame.Rect(550, 300, 100, ALL_RECTANGLES_HEIGHT)

    def handle_events(self, events):
        """
        Initializes event handling in start menu
        Args:
            events (list): List of events to be handled
        Returns: None
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.is_active = False
                return
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.cat_button.collidepoint(event.pos):
                    self.selected_pet = 'cat'
                elif self.dog_button.collidepoint(event.pos):
                    self.selected_pet = 'dog'
                elif self.start_button.collidepoint(event.pos) and self.pet_name and self.selected_pet:
                    self.is_active = False
            
                if self.input_box.collidepoint(event.pos):
                    self.active_input = True
                else:
                   self.active_input = False
                    
            if event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.pet_name = self.pet_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.pet_name:
                            self.is_active = False
                    else:
                        self.pet_name += event.unicode
                        
    def draw(self):
        """
        Draws the start menu screen with interactive elements
        Args: None
        Returns: None
        """
        # Loads background
        image_file = os.path.join("assets", "images", "game_background.jpg")
        background = pygame.image.load(image_file)
        background = pygame.transform.scale(background, (800, 600))
        self.screen.blit(background, (0, 0))        

        # Renders title
        title = self.font.render("Pixel Paws Pet Simulator", True, (START_MENU_TEXT_COLOR))
        self.screen.blit(title, (85, 50))
        
        # Gets mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Buttons with their properties
        button_data = [
            (self.cat_button, CAT_BUTTON_COLOR, "Cat", 2, 8),
            (self.dog_button, DOG_BUTTON_COLOR, "Dog", 2, 8)
        ]
        
        # Checks if pet buttons are hovered
        for button, color, text, x_offset, y_offset in button_data:
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (BUTTON_HOVER_COLOR), button)
            else:
                pygame.draw.rect(self.screen, color, button)
            
            # Renders pet selection button text
            button_text = self.font.render(text, True, (START_MENU_TEXT_COLOR))
            self.screen.blit(button_text, (button.x + x_offset, button.y + y_offset))
        
        # Draws input box and text
        pygame.draw.rect(self.screen, (NAME_RECTANGLE_COLOR), self.input_box, 2)
        input_text = self.font.render(self.pet_name, True, (START_MENU_TEXT_COLOR))
        name_text = self.font.render("Name Your Pet:", True, (START_MENU_TEXT_COLOR))
        self.screen.blit(name_text, (self.input_box.x - 45, self.input_box.y - 70))
        self.screen.blit(input_text, (self.input_box.x + 5, self.input_box.y + 5))    
        
        # Checks hover over start button
        if self.start_button.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (BUTTON_HOVER_COLOR), self.start_button)
        else:
            pygame.draw.rect(self.screen, START_BUTTON_COLOR, self.start_button)
            
        # Draws start button text
        start_text = self.font.render("Start", True, (START_MENU_TEXT_COLOR))
        self.screen.blit(start_text, (self.start_button.x + 20, self.start_button.y + 8))
        
    def get_pet_name(self):
        """
        Returns the pet name entered by the user
        Args: None
        Returns:
            pet_name (str): The name of the pet
        """
        return self.pet_name
    
    def get_selected_pet(self):
        """
        Returns the selected pet
        Args: None
        Returns:
            selected_pet: The pet selection ('cat' or 'dog')
        """
        return self.selected_pet