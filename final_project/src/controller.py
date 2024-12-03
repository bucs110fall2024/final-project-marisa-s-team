import pygame
import os
import sys
from src.startmenu import StartMenu
from src.game import Game

class Controller:
    def __init__(self):
        """
        Initializes the Controller object
        Args: None
        Returns: None
        """
        pygame.init()
        print("Controller initialized.")
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pixel Paws Pet Simulator")
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        self.font = pygame.font.Font(font_path, 30)
        self.is_running = True
        
    def mainloop(self):
        """
        Initializes mainloop of Controller object
        Args: None
        Returns: None
        """
        print("Starting main loop")
        
        pygame.mixer.init()   
        music_file = os.path.join("assets", "music", "background_music.mp3")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=-1, start=0.0)
               
        start_menu = StartMenu(self.screen, self.font)
        while start_menu.is_active:
            events = pygame.event.get()
            start_menu.handle_events(events)
            
            for event in events:
                if event.type == pygame.QUIT:
                    start_menu.is_active = False
                    self.is_running = False
                    break
            
            start_menu.draw()
            pygame.display.flip()
            
        pet_name = start_menu.get_pet_name()
        selected_pet = start_menu.get_selected_pet()
        print(f"Pet Name: {pet_name}, Selected Pet: {selected_pet}")
        
        game = Game(self.screen, self.font, pet_name, selected_pet, start_menu.cat_button, start_menu.dog_button, start_menu.start_button)
            
        while self.is_running:
            events = pygame.event.get()
            
            game.handle_events(events)
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                    break
                
            delta_time = pygame.time.get_ticks() / 1000.0
            game.update(delta_time)
            game.draw()
            
            if game.is_game_over():
                self.game_over(game)
                break
            
            pygame.display.flip()
        
        print("Exiting main loop")
        
        pygame.quit()
        sys.exit()
        
    def game_over(self, game):
        """
        Initializes game over screen
        Args:
            game (object): game model
        Returns: None
        """
        background_image_path = os.path.join("assets", "images", "game_over_background.jpg")
        background = pygame.image.load(background_image_path)
        background = pygame.transform.scale(background, (800, 600))
        
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        font = pygame.font.Font(font_path, 20)
        game_over_text = font.render(f"{game.pet_name} Died!", True, (255, 255, 0))
        option_game_over_text = font.render("Press 'R' to restart or 'Q' to quit.", True, (255, 255, 0))
        
        self.screen.blit(background, (0, 0))        
        self.screen.blit(game_over_text, (290, 100))
        self.screen.blit(option_game_over_text, (110, 150))
        pygame.display.flip()
        
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.mainloop()
                    elif event.key == pygame.K_q:
                        self.is_running = False
                        waiting_for_input = False