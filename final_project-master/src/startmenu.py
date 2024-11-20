import pygame

class StartMenu:
    def __init__(self, screen, font):
        """
        Initializes StartMenu object
        Args:
            screen (display): display of start menu
            font (object): font of start menu text
        Returns: None
        """
        self.screen = screen
        self.font = font
        self.pet_name = ''
        self.selected_pet = None
        self.is_active = True
        
        self.start_button = pygame.Rect(300, 300, 200, 50)
        self.input_box = pygame.Rect(300, 200, 200, 50)
        self.active_input = False
        self.cat_button = pygame.Rect(150, 300, 100, 50)
        self.dog_button = pygame.Rect(550, 300, 100, 50)
        
    def handle_events(self, events):
        """
        Initializes event handling in StartMenu
        Args:
            events (event): event that occurs in StartMenu
        Returns: None
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.is_active = False
                print("Quit event detected")
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.cat_button.collidepoint(event.pos):
                    self.selected_pet = 'cat'
                    print("Cat selected")
                elif self.dog_button.collidepoint(event.pos):
                    self.selected_pet = 'dog'
                    print("Dog selected")
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
                            print(f"Pet name entered: {self.pet_name}")
                    else:
                        self.pet_name += event.unicode
                        
    def draw(self):
        """
        Draws StartMenu screen
        Args: None
        Returns: None
        """
        self.screen.fill((232, 153, 227))
        
        title = self.font.render("Pixel Paws Pet Simulator", True, (255, 255, 255))
        self.screen.blit(title, (300, 50))
        
        pygame.draw.rect(self.screen, (255, 255, 255), self.cat_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.dog_button)

        cat_text = self.font.render("Cat", True, (0, 0, 0))
        dog_text = self.font.render("Dog", True, (0, 0, 0))
        self.screen.blit(cat_text, (self.cat_button.x + 35, self.cat_button.y + 15))
        self.screen.blit(dog_text, (self.dog_button.x + 35, self.dog_button.y + 15))
        
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
        input_text = self.font.render(self.pet_name, True, (255, 255, 255))
        self.screen.blit(input_text, (self.input_box.x + 5, self.input_box.y + 5))
        
        pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)
        start_text = self.font.render("Start", True, (0, 0, 0))
        self.screen.blit(start_text, (self.start_button.x + 80, self.start_button.y + 15))
        
    def get_pet_name(self):
        """
        Returns pet name
        Args: None
        Returns:
            self.pet_name: name of pet
        """
        return self.pet_name
    
    def get_selected_pet(self):
        """
        Returns selected pet
        Returns:
            self.selected_pet: pet selection (cat or dog)
        """
        return self.selected_pet