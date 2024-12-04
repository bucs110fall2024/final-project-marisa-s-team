import pygame
import os
import sys
from src.startmenu import StartMenu
from src.highscore import HighScore
from src.game import Game

# Constant
GAME_OVER_TEXT_COLOR = (255, 255, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHt = 600
FPS = 60


class Controller:
    """
    The Controller class which manages the game loop, main menu, and game over screen
    """
    def __init__(self):
        """
        Initializes the Controller object
        Args: None
        Returns: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHt))
        pygame.display.set_caption("Pixel Paws Pet Simulator")
        self.font = pygame.font.Font(os.path.join("assets", "fonts", "Daydream.ttf"), 30) #
       
        # Game State
        self.is_running = True
        self.high_score_manager = HighScore()
       
    def mainloop(self):
        """
        Initializes mainloop of Controller object
        Args: None
        Returns: None
        """
        pygame.mixer.init()  
        music_file = os.path.join("assets", "music", "background_music.mp3")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=-1, start=0.0)
       
        # Main menu loop      
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
       
        # Gets pet name and selection from start menu    
        pet_name = start_menu.get_pet_name()
        selected_pet = start_menu.get_selected_pet()
       
        game = Game(self.screen, self.font, pet_name, selected_pet, start_menu.cat_button, start_menu.dog_button, start_menu.start_button)
       
        # Game loop  
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
       
        pygame.quit()
        sys.exit()
       
    def game_over(self, game):
        """
        Initializes game over screen
        Args:
            game (object): The game model
        Returns: None
        """
        # Creates game over screen background
        background_image_path = os.path.join("assets", "images", "game_over_background.jpg")
        background = pygame.image.load(background_image_path)
        background = pygame.transform.scale(background, (800, 600))
       
        font_path = os.path.join("assets", "fonts", "Daydream.ttf")
        font = pygame.font.Font(font_path, 20)
        game_over_text = font.render("Your Pet Died!", True, (GAME_OVER_TEXT_COLOR))
        option_game_over_text = font.render("Press 'R' to restart or 'Q' to quit.", True, (GAME_OVER_TEXT_COLOR))
       
        final_score = game.get_score()
        self.high_score_manager.update_high_score(final_score)
        high_score_text = font.render(f"High Score: {self.high_score_manager.get_high_score()}", True, (GAME_OVER_TEXT_COLOR))
       
        # Blits background and game over text
        self.screen.blit(background, (0, 0))        
        self.screen.blit(game_over_text, (280, 100))
        self.screen.blit(option_game_over_text, (110, 150))
        self.screen.blit(high_score_text, (280, 200))
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