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
            self.pet = Pet(350, 250, "assets/cat.png")
        elif self.selected_pet == 'dog':
            self.pet = Pet(350, 250, "assets/dog.png")
            
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
                self.running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons['pet'].collidepoint(event.pos):
                    self.pet.pet()
                    print(f"Happiness: {self.pet.happiness}")
                elif self.buttons['feed'].collidepoint(event.pos):
                    self.pet.feed()
                    print(f"Hunger: {self.pet.hunger}")
                elif self.buttons['play'].collidepoint(event.pos):
                    self.pet.play()
                    print(f"Health: {self.pet.health}")
                
            if event.type == pygame.KEYDOWN:
                if self.active_input:
                    if event.key == pygame.K_BACKSPACE:
                        self.pet_name = self.pet_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.pet_name:
                            self.is_active = False
                    else:
                        self.pet_name += event.unicode
                        
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
            
    def draw(self):
        """
        Draws screen, buttons, and status bars
        Args: None
        Returns: None
        """
        self.screen.fill((232, 153, 227))
        
        self.pet.draw(self.screen)
        
        hunger, health, happiness = self.pet.get_status()
            
        delta_time = pygame.time.get_ticks() / 1000.0
        
        self.health_bar.update(delta_time)
        self.hunger_bar.update(delta_time)
        self.happiness_bar.update(delta_time)
        
        self.health_bar.draw(self.screen)
        self.hunger_bar.draw(self.screen)
        self.happiness_bar.draw(self.screen)
        
        pygame.draw.rect(self.screen, (0, 255, 0), self.buttons['play'])
        pygame.draw.rect(self.screen, (0, 255, 0), self.buttons['feed'])
        pygame.draw.rect(self.screen, (0, 255, 0), self.buttons['pet'])
            
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        button_font = pygame.font.Font(font_path, 20)
        play_text = button_font.render("Play", True, (0, 0, 0))
        feed_text = button_font.render("Feed", True, (0, 0, 0))
        pet_text = button_font.render("Pet", True, (0, 0, 0))
        
        self.screen.blit(play_text, (self.buttons['play'].x + 30, self.buttons['play'].y + 15))
        self.screen.blit(feed_text, (self.buttons['feed'].x + 30, self.buttons['feed'].y + 15))
        self.screen.blit(pet_text, (self.buttons['pet'].x + 35, self.buttons['pet'].y + 15))
        
    def is_game_over(self):
        """
        Determines whether game is over
        Returns:
            self.health_bar.value, self.hunger_bar.value, self.happiness_bar.value: values of pet's attributes
        """
        return self.health_bar.value == 0 or self.hunger_bar.value == 0 or self.happiness_bar.value == 0
            
        