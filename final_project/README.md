
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Pixel Paws Pet Simulator
## CS110 Final Project  Fall, 2024

## Team Members

Marisa Keefe

***

## Project Description

My game is going to be a pet simulator. I want the user to be able to click buttons to maintain the health, happiness, and hunger of the animal. If the user does not keep these ever-depleting status bars going, the pet dies.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Animal on screen
2. Three buttons for user to click
3. Updating health, happiness, and hunger bar that continuously deplete until user hits buttons
4. Game over screen
5. Start menu including naming pet

### Classes

- StartMenu:
    - Creates start menu screen with bar to type pet name in, cat or dog selection button, and start button
- Pet:
    - Creates pet objects for cat and dog selection importing a picture as the pet on screen
- StatusBar:
    - Creates status bars for health, happiness, and hunger that deplete with time and determine the life of the pet
- Game:
    - Creates game screen where the pet, buttons, and status bars are and the user can interact with the buttons
- Controller:
    - Puts the objects together, creating the game itself and a game over screen

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Q key pressed")
                    self.running = False
                elif event.key == pygame.K_BACKSPACE:
                    self.pet_name = self.pet_name[:-1]
                elif event.key == pygame.K_RETURN:
                    if self.pet_name:
                        self.is_active = False
                    else:
                        self.pet_name += event.unicode