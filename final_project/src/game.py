import pygame
import os
from src.pet import Pet
from src.statusbar import StatusBar

class Game:
    def __init__(self, screen, font, pet_name, selected_pet, cat_button, dog_button, start_button):
        """
        Initializes Game object
        Args:
            screen (display): game display
            font (font): font used in status bars and buttons
            pet_name (str): name of pet
            selected_pet (str): selected pet 
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
        
        self.health_bar = StatusBar(500, 20, 300, 40, 100, "Health", 0.001)
        self.hunger_bar = StatusBar(500, 80, 300, 40, 100, "Hunger", 0.005)
        self.happiness_bar = StatusBar(500, 140, 300, 40, 100, "Happiness", 0.003)
        
        if self.selected_pet == 'cat':
            self.pet = Pet(350, 250, "assets/images/cat.png")
        elif self.selected_pet == 'dog':
            self.pet = Pet(350, 250, "assets/images/dog.png")
            
        self.buttons = {
            'play': pygame.Rect(50, 460, 100, 50),
            'feed': pygame.Rect(50, 520, 100, 50),
            'pet': pygame.Rect(50, 400, 100, 50)
        }
        
    def handle_events(self, events):
        """
        Initializes event handling in game
        Args:
            events (event): events that occur within game
        Returns: None
        """        
        for event in events:
            if event.type == pygame.QUIT:
                print("Quit event detected") #
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons['pet'].collidepoint(event.pos):
                    self.pet.pet()
                    self.happiness_bar.value = self.pet.happiness
                    print(f"Happiness: {self.pet.happiness}")
                elif self.buttons['feed'].collidepoint(event.pos):
                    self.pet.feed()
                    self.hunger_bar.value = self.pet.hunger
                    print(f"Hunger: {self.pet.hunger}")
                elif self.buttons['play'].collidepoint(event.pos):
                    self.pet.play()
                    self.health_bar.value = self.pet.health
                    print(f"Health: {self.pet.health}")

    def update(self, delta_time):
        """
        Updates status bars
        Args:
            delta_time (time): time
        Returns: None
        """
        self.health_bar.update(delta_time)
        self.hunger_bar.update(delta_time)
        self.happiness_bar.update(delta_time)
        
        if self.is_game_over():
            self.running = False
            return True
        
        return False
        
    def draw(self):
        """
        Draws screen, buttons, and status bars
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
        
    def is_game_over(self):
        """
        Determines whether game is over
        Returns:
            self.health_bar.value, self.hunger_bar.value, self.happiness_bar.value: values of pet's attributes
        """
        return self.health_bar.value == 0 or self.hunger_bar.value == 0 or self.happiness_bar.value == 0