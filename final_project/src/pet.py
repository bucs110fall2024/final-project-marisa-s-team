import pygame

class Pet:
    def __init__(self, x, y, image_path):
        """
        Initializes Pet object
        Args:
            x (int): x-coordinate
            y (int): y-coordinate
            image_path (str): path to pet image
        Returns: None
        """
        self.x = x
        self.y = y
        self.image_path = image_path
        
        self.image = pygame.image.load(image_path) 
        self.image = pygame.transform.scale(self.image, (350, 350))
        
        self.alive = True
        self.health = 100
        self.hunger = 100
        self.happiness = 100
        self.health_depletion_rate = 0.00001
        self.hunger_depletion_rate = 0.000005
        self.happiness_depletion_rate = 0.003
    
    def update(self, delta_time):
        """
        Updates hunger, health, and happiness of pet
        Args: None
        Returns: None
        """
        if self.alive:
            if self.health > 0:
                self.health -= 0.03
            if self.hunger > 0:
                self.hunger -= 0.05
            if self.happiness > 0:
                self.happiness -= 0.05
            
        if self.hunger <= 0 or self.health <= 0 or self.happiness <= 0:
            self.die()
            
        # print(f"Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}") #

        self.health -= self.health_depletion_rate * delta_time
        self.hunger -= self.hunger_depletion_rate * delta_time
        self.happiness -= self.happiness_depletion_rate * delta_time
            
        self.health = max(0, self.health)
        self.hunger = max(0, self.hunger)
        self.happiness = max(0, self.happiness)
        
    def die(self):
        """
        Defines death of pet
        Args: None
        Returns: None
        """
        self.alive = False
        
    def play(self):
        """
        Defines how long the pet can go without being played with before health depletes
        Args: None
        Returns: None
        """
        # if self.alive:
            # self.health = min(self.health + 15, 100)  
        self.health = min(100, self.health + 10)
              
    def feed(self):
        """
        Defines how hungry pet can be before hunger depletes
        Args: None
        Returns: None
        """
        # if self.alive:
            # self.hunger = min(self.hunger + 20, 100)
        self.hunger = min(100, self.hunger + 20)
    
    def pet(self):
        """
        Defines how long the pet can go without pets before happiness depletes
        Args: None
        Returns: None
        """
        # if self.alive:
            # self.happiness = min(self.happiness + 10, 100)
        self.happiness = min(100, self.happiness + 10)
    
    def get_status(self):
        """
        Gets status of pet's health, hunger, and happiness
        Args: None
        Returns:
            self.health, self.hunger, self.happiness: status of pet's bars
        """
        return self.health, self.hunger, self.happiness
        
    def draw(self, screen):
        """
        Draws image of pet
        Args:
            screen (display): screen blit
        Returns: None
        """
        screen.blit(self.image, (self.x - 80, self.y - 20))