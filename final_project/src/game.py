import pygame
import os
from src.pet import Pet
from src.statusbar import StatusBar

# Constants
HEALTH_DEPLETION_RATE = 0.0001
HUNGER_DEPLETION_RATE = 0.0005
HAPPINESS_DEPLETION_RATE = 0.0008
PET_X_POSITION = 350
PET_Y_POSITION = 250
TIME_OF_ITEM_ON_SCREEN = 500
BUTTON_COLOR = (184, 245, 241)
BUTTON_TEXT_COLOR = (255, 255, 255)
NAME_TEXT_COLOR = (255, 255, 255)
INTERACTION_TIMERS = 0

class Game:
    """
    The Game class which creates the game logic, event handling, updates status bars, 
    draws the screen, and reacts to user ineractions
    """
    def __init__(self, screen, font, pet_name, selected_pet, cat_button, dog_button, start_button):
        """
        Initializes the Game object
        Args:
            screen (pygame.Surface): The game display surface
            font (pygame.font.Font): Font object for rendering text
            pet_name (str): The name of the pet
            selected_pet (str): The type of pet selected ('cat' or 'dog')
            cat_button (pygame.Rect): The cat selection button
            dog_button (pygame.Rect): The dog selection button
            start_button (pygame.Rect): The start button
        Returns: None
        """
        self.screen = screen
        self.font = font
        self.pet_name = pet_name
        self.selected_pet = selected_pet
        self.running = True
        self.cat_button = cat_button
        self.dog_button = dog_button
        self.start_button = start_button
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        
        self.health_bar = StatusBar(500, 20, 300, 40, 100, "Health", HEALTH_DEPLETION_RATE)
        self.hunger_bar = StatusBar(500, 80, 300, 40, 100, "Hunger", HUNGER_DEPLETION_RATE)
        self.happiness_bar = StatusBar(500, 140, 300, 40, 100, "Happiness", HAPPINESS_DEPLETION_RATE)
        
        if self.selected_pet == 'cat':
            self.pet = Pet(PET_X_POSITION, PET_Y_POSITION, "assets/images/cat.png")
        elif self.selected_pet == 'dog':
            self.pet = Pet(PET_X_POSITION, PET_Y_POSITION, "assets/images/dog.png")
        
        # Loads images prompted by interactive buttons
        self.food_bowl_image = pygame.image.load("assets/images/food_bowl.png")
        self.heart_image = pygame.image.load("assets/images/heart.png")
        self.ball_image = pygame.image.load("assets/images/ball.png")
        
        # Scales images
        self.food_bowl_image = pygame.transform.scale(self.food_bowl_image, (100, 100))
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.ball_image = pygame.transform.scale(self.ball_image, (80, 80))

        # Starts interaction flags and timers
        self.show_food_bowl = False
        self.show_heart = False
        self.show_ball = False
        
        self.food_bowl_timer = INTERACTION_TIMERS
        self.heart_timer = INTERACTION_TIMERS
        self.ball_timer = INTERACTION_TIMERS
        
        # Creates interactive buttons
        self.buttons = {
            'play': pygame.Rect(50, 520, 100, 50),
            'feed': pygame.Rect(175, 520, 100, 50),
            'pet': pygame.Rect(300, 520, 100, 50)
        }
        
        
    def handle_events(self, events):
        """
        Initializes event handling in the game loop
        Args:
            events (list): List of events that need to be processed in the game
        Returns: None
        """        
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons['pet'].collidepoint(event.pos):
                    self.pet.pet()
                    self.happiness_bar.value = self.pet.happiness
                    self.show_heart = True
                    self.heart_timer = pygame.time.get_ticks()
                elif self.buttons['feed'].collidepoint(event.pos):
                    self.pet.play()
                    self.health_bar.value = self.pet.health
                    self.show_food_bowl = True
                    self.food_bowl_timer = pygame.time.get_ticks()
                elif self.buttons['play'].collidepoint(event.pos):
                    self.pet.feed()
                    self.hunger_bar.value = self.pet.hunger
                    self.show_ball = True
                    self.ball_timer = pygame.time.get_ticks()

    def update(self, delta_time):
        """
        Updates status bars and checks if any bars depleted
        Args:
            delta_time (int): The time difference between the frames
        Returns: 
            bool: Returns True if game is over, or False if it is not over
        """
        self.pet.update(delta_time)
        
        self.score = (pygame.time.get_ticks() - self.start_time) // 1000
        
        self.health_bar.update(delta_time)
        self.hunger_bar.update(delta_time)
        self.happiness_bar.update(delta_time)
                
        if self.is_game_over():
            self.running = False
            return True
        
        current_time = pygame.time.get_ticks()
        if current_time - self.food_bowl_timer > TIME_OF_ITEM_ON_SCREEN:
            self.show_food_bowl = False
        if current_time - self.heart_timer > TIME_OF_ITEM_ON_SCREEN:
            self.show_heart = False
        if current_time - self.ball_timer > TIME_OF_ITEM_ON_SCREEN:
            self.show_ball = False
            
        return False
        
    def draw(self):
        """
        Draws the screen, buttons, pet, and status bars
        Args: None
        Returns: None
        """
        # Creates background
        background_image_path = os.path.join("assets", "images", "start_menu_background.jpg")
        background = pygame.image.load(background_image_path)
        background = pygame.transform.scale(background, (800, 600))
        self.screen.blit(background, (0, 0))
        
        self.pet.draw(self.screen)
        
        # Updates status bars
        hunger, health, happiness = self.pet.get_status()
        self.health_bar.value = health
        self.hunger_bar.value = hunger
        self.happiness_bar.value = happiness
        
        # Draws status bars
        self.health_bar.draw(self.screen)
        self.hunger_bar.draw(self.screen)
        self.happiness_bar.draw(self.screen)
        
        # Gets mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Button hover effect
        for button_key, button_rect in self.buttons.items():
            if button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (150, 200, 200), button_rect)
            else:
                pygame.draw.rect(self.screen, BUTTON_COLOR, button_rect)
                
        # Renders button labels    
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        button_font = pygame.font.Font(font_path, 20)
        play_text = button_font.render("Play", True, (BUTTON_TEXT_COLOR))
        feed_text = button_font.render("Feed", True, (BUTTON_TEXT_COLOR))
        pet_text = button_font.render("Pet", True, (BUTTON_TEXT_COLOR))
        score_text = self.font.render(f"Score: {self.score}", True, (BUTTON_TEXT_COLOR))
           
        # Blit texts
        self.screen.blit(score_text, (10, 60))
        self.screen.blit(play_text, (self.buttons['play'].x + 10, self.buttons['play'].y + 15))
        self.screen.blit(feed_text, (self.buttons['feed'].x + 10, self.buttons['feed'].y + 15))
        self.screen.blit(pet_text, (self.buttons['pet'].x + 20, self.buttons['pet'].y + 15))
        
        # Displays pet name
        pet_name_text = self.font.render(f"Name: {self.pet_name}", True, (NAME_TEXT_COLOR))
        self.screen.blit(pet_name_text, (10, 10))
        
        # Positions images put on screen by user interaction        
        self.food_bowl_position = (self.pet.x - 60, self.pet.y + 160)
        self.heart_position = (self.pet.x + 70, self.pet.y - 50)
        self.ball_position = (self.pet.x - 80, self.pet.y - 70)

        if self.show_food_bowl:
            self.screen.blit(self.food_bowl_image, self.food_bowl_position)
        if self.show_heart:
            self.screen.blit(self.heart_image, self.heart_position)
        if self.show_ball:
            self.screen.blit(self.ball_image, self.ball_position)
    
    def get_score(self):
        """
        Returns the current score of the player
        Args: None
        Returns: score (int): The current score of the player
        """
        return self.score
                
    def is_game_over(self):
        """
        Determines whether any status bars have reached 0
        Args: None
        Returns:
            bool: Returns True if any status bars reach 0
        """
        return self.health_bar.value == 0 or self.hunger_bar.value == 0 or self.happiness_bar.value == 0
    
    # uPDATE