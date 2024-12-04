import pygame

# Constants
FULL_STATUS = 100
END_STATUS = 0
HEALTH_DEPLETION_RATE = 0.0001
HUNGER_DEPLETION_RATE = 0.0005
HAPPINESS_DEPLETION_RATE = 0.0008

class Pet:
    """
    Pet class that represents the state of the pet (health, hunger, happiness)
    and allows user to interact with the pet
    """
    def __init__(self, x, y, image_path):
        """
        Initializes Pet object and it's position, image, and status
        Args:
            x (int): The x-coordinate of the pet
            y (int): The y-coordinate of the pet
            image_path (str): The path to the pet image
        Returns: None
        """
        self.x = x
        self.y = y
        self.image_path = image_path
        
        # Loads pet images and scales them
        self.image = pygame.image.load(image_path) 
        self.image = pygame.transform.scale(self.image, (350, 350))
        
        # Pet status
        self.alive = True
        self.health = FULL_STATUS
        self.hunger = FULL_STATUS
        self.happiness = FULL_STATUS
        
        self.health_depletion_rate = HEALTH_DEPLETION_RATE
        self.hunger_depletion_rate = HUNGER_DEPLETION_RATE
        self.happiness_depletion_rate = HAPPINESS_DEPLETION_RATE

    def update(self, delta_time):
        """
        Updates the hunger, health, and happiness of the pet over time
        Args:
            delta_time (float): The time passed since the last status update
        Returns: None
        """
        if self.alive:
            if self.health > END_STATUS:
                self.health -= 0.03
            if self.hunger > END_STATUS:
                self.hunger -= 0.05
            if self.happiness > END_STATUS:
                self.happiness -= 0.05
        
        # Applies status depletion rate    
        self.health -= self.health_depletion_rate * delta_time
        self.hunger -= self.hunger_depletion_rate * delta_time
        self.happiness -= self.happiness_depletion_rate * delta_time
        
        # Makes sure values do not go below the end status   
        self.health = max(END_STATUS, self.health)
        self.hunger = max(END_STATUS, self.hunger)
        self.happiness = max(END_STATUS, self.happiness)
        
        if self.hunger <= END_STATUS or self.health <= END_STATUS or self.happiness <= END_STATUS:
            self.die()
        
    def die(self):
        """
        Defines death of pet
        Args: None
        Returns: None
        """
        self.alive = False
        
    def play(self):
        """
        Increases the pet's happiness by 10 when the user hits 'play'
        Args: None
        Returns: None
        """
        self.health = min(100, self.health + 10)
              
    def feed(self):
        """
        Increases the pet's hunger by 20 when the user hits 'feed'
        Args: None
        Returns: None
        """
        self.hunger = min(100, self.hunger + 20)
    
    def pet(self):
        """
        Increases the pet's happiness by 10 when the user hits 'pet'
        Args: None
        Returns: None
        """
        self.happiness = min(100, self.happiness + 10)
    
    def get_status(self):
        """
        Returns the status of the pet's health, hunger, and happiness
        Args: None
        Returns:
            health, hunger, happiness (tuple): Status values
        """
        return self.health, self.hunger, self.happiness
        
    def draw(self, screen):
        """
        Draws the image of the pet
        Args:
            screen (pygame.Surface): The screen surface for the pet image
        Returns: None
        """
        screen.blit(self.image, (self.x - 80, self.y - 20))