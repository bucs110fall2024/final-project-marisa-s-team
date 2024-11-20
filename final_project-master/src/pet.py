import pygame

class Pet:
    def __init__(self, x, y, image_path):
        """
        Initializes Pet object
        Args:
            x (int): x-coordinate
            y (int): y-coordinate
            image_path (path): image path
        Returns: None
        """
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (350, 350))
        
        self.alive = True
        self.hunger = 100
        self.health = 100
        self.happiness = 100
    
    def update(self):
        """
        Updates hunger, health, and happiness of pet
        Args: None
        Returns: None
        """
        if self.alive:
            if self.hunger > 0:
                self.hunger -= 0.05
            if self.health > 0:
                self.health -= 0.03
            if self.happiness > 0:
                self.happiness -= 0.05
            
        if self.hunger <= 0 or self.health <= 0 or self.happiness <=0:
            self.die()
            
    def die(self):
        """
        Defines death of pet
        Args: None
        Returns: None
        """
        self.alive = False
        
    def feed(self):
        """
        Defines how hungry pet can be before hunger depletes
        Args: None
        Returns: None
        """
        if self.alive:
            self.hunger = min(self.hunger + 20, 100)
    
    def pet(self):
        """
        Defines how long the pet can go without pets before happiness depletes
        Args: None
        Returns: None
        """
        if self.alive:
            self.happiness = min(self.happiness + 10, 100)
            
    def play(self):
        """
        Defines how long the pet can go without being played with before health depletes
        Args: None
        Returns: None
        """
        if self.alive:
            self.health = min(self.health + 15, 100)
    
    def get_status(self):
        """
        Gets status of pet's hunger, health, and happiness
        Args: None
        Returns:
            self.hunger, self.health, self.happiness: status of pet's bars
        """
        return (self.hunger, self.health, self.happiness)
    
    def draw(self, screen):
        """
        Draws image of pet
        Args:
            screen (display): screen blit
        Returns: None
        """
        screen.blit(self.image, (self.x, self.y))