import json
import os

# Constant
HIGH_SCORE_FILE = "etc/highscore.json"

class HighScore:
    """
    HighScore class which loads, saves, and updates the high score
    """
    def __init__(self):
        """
        Initializes Highscore object which starts at 0 and loads previous high score
        Args: None
        Returns: None
        """
        self.high_score = 0
        self.load_high_score()
        
    def load_high_score(self):
        """
        Loads the high score from the JSON file and if the file does not exist or is invalid, sets the high score to 0
        Args: None
        Returns: None
        """
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as file:
                try:
                    data = json.load(file)
                    self.high_score = data.get("high_score", 0)
                except (ValueError, json.JSONDecodeError):
                    self.high_score = 0
        else:
            self.high_score = 0
    
    def save_high_score(self):
        """
        Saves the current high score to the JSON file
        Args: None
        Returns: None
        """
        data = {"Your High Score": self.high_score}
        with open(HIGH_SCORE_FILE, "w") as file:
            json.dump(data, file, indent=4)
    
    def update_high_score(self, new_score):
        """
        Updates if the new score is higher than the previous high score
        Args:
            new_score (int): The newest high score
        Returns: None
        """
        if new_score > self.high_score:
            self.high_score = new_score
            self.save_high_score()
    
    def get_high_score(self):
        """
        Returns the current high score
        Args: None
        Returns: high_score (int): The current high score
        """
        return self.high_score