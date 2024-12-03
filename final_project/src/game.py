import pygame
import os
from src.pet import Pet
from src.statusbar import StatusBar

class Game:
    def __init__(self, screen, font, pet_name, selected_pet, cat_button, dog_button, start_button):
        """
        Initializes the Game object
        Args:
            screen (pygame.Surface): The game display surface
            font (pygame.font.Font): Font object for rendering text
            pet_name (str): The name of the pet
            selected_pet (str): The type of pet selected ('cat' or 'dog')
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
        
        self.health_bar = StatusBar(500, 20, 300, 40, 100, "Health", 0.01)
        self.hunger_bar = StatusBar(500, 80, 300, 40, 100, "Hunger", 0.05)
        self.happiness_bar = StatusBar(500, 140, 300, 40, 100, "Happiness", 0.08)
        
        # Pet selection
        if self.selected_pet == 'cat':
            self.pet = Pet(350, 250, "assets/images/cat.png")
        elif self.selected_pet == 'dog':
            self.pet = Pet(350, 250, "assets/images/dog.png")
        
        # Images triggered by selected buttons
        self.food_bowl_image = pygame.image.load("assets/images/food_bowl.png")
        self.heart_image = pygame.image.load("assets/images/heart.png")
        self.ball_image = pygame.image.load("assets/images/ball.png")
        
        # Scale of images
        self.food_bowl_image = pygame.transform.scale(self.food_bowl_image, (100, 100))
        self.heart_image = pygame.transform.scale(self.heart_image, (50, 50))
        self.ball_image = pygame.transform.scale(self.ball_image, (80, 80))

        # Interaction flags
        self.show_food_bowl = False
        self.show_heart = False
        self.show_ball = False
        
        # Interaction timers
        self.food_bowl_timer = 0
        self.heart_timer = 0
        self.ball_timer = 0
        
        # Interactive buttons  
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
        
        self.health_bar.update(delta_time)
        self.hunger_bar.update(delta_time)
        self.happiness_bar.update(delta_time)
        
        if self.is_game_over():
            self.running = False
            return True
        
        current_time = pygame.time.get_ticks()
        if current_time - self.food_bowl_timer > 500:
            self.show_food_bowl = False
        if current_time - self.heart_timer > 500:
            self.show_heart = False
        if current_time - self.ball_timer > 500:
            self.show_ball = False
            
        return False
        
    def draw(self):
        """
        Draws the screen, buttons, pet, and status bars
        Args: None
        Returns: None
        """
        background_image_path = os.path.join("assets", "images", "start_menu_background.jpg")
        background = pygame.image.load(background_image_path)
        background = pygame.transform.scale(background, (800, 600))
        self.screen.blit(background, (0, 0))
        
        self.pet.draw(self.screen)
        
        hunger, health, happiness = self.pet.get_status()
        self.health_bar.value = health
        self.hunger_bar.value = hunger
        self.happiness_bar.value = happiness
        
        self.health_bar.draw(self.screen)
        self.hunger_bar.draw(self.screen)
        self.happiness_bar.draw(self.screen)
        
        pygame.draw.rect(self.screen, (184, 245, 241), self.buttons['play'])
        pygame.draw.rect(self.screen, (184, 245, 241), self.buttons['feed'])
        pygame.draw.rect(self.screen, (184, 245, 241), self.buttons['pet'])
            
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        button_font = pygame.font.Font(font_path, 20)
        play_text = button_font.render("Play", True, (255, 255, 255))
        feed_text = button_font.render("Feed", True, (255, 255, 255))
        pet_text = button_font.render("Pet", True, (255, 255, 255))
        
        self.screen.blit(play_text, (self.buttons['play'].x + 10, self.buttons['play'].y + 15))
        self.screen.blit(feed_text, (self.buttons['feed'].x + 10, self.buttons['feed'].y + 15))
        self.screen.blit(pet_text, (self.buttons['pet'].x + 20, self.buttons['pet'].y + 15))
        
        pet_name_text = self.font.render(f"Pet Name: {self.pet_name}", True, (255, 255, 255))
        self.screen.blit(pet_name_text, (10, 10))
                
        self.food_bowl_position = (self.pet.x - 60, self.pet.y + 160)
        self.heart_position = (self.pet.x + 70, self.pet.y - 50)
        self.ball_position = (self.pet.x - 80, self.pet.y - 70)

        if self.show_food_bowl:
            self.screen.blit(self.food_bowl_image, self.food_bowl_position)
        if self.show_heart:
            self.screen.blit(self.heart_image, self.heart_position)
        if self.show_ball:
            self.screen.blit(self.ball_image, self.ball_position)
        
    def is_game_over(self):
        """
        Determines whether any status bars have reached 0, ending the game
        Args: None
        Returns:
            bool: Returns True if any status bars reach 0
        """
        return self.health_bar.value == 0 or self.hunger_bar.value == 0 or self.happiness_bar.value == 0