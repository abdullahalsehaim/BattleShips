# Battleships Game

This 

## Gameplay
+ Player enters their name into the terminal.
+ Player is then asked to enter a board size and a number of ships.
+ Player can then choose row and column coordinates for the number of ships they have selected.
+ Both boards are then printed, the players chosen coordinates will appear as `@`, computers coordinates will not be visible.
+ As players makes guesses on the board they are displayed as `X`, when a ship is hit and subsequently sank it is displayed as `*`.
+ Between every round of play the player has the option to either continue the game or exit. 
+ If the player chooses to continue each time, the game proceeds until a sides ships are completely sunk.
+ Whoever sinks all their opponents boats first wins

## Features

### Existing Features

##### Board Size
+ Players can set the size of the board to modify the level of difficulty slightly.
+ Board size can be betwen 4 and 8.

#### Number of Ships
+ Players can select the number of ships in the game to also modify the level of difficulty
+ Number of ships can be between 2 and 6.

#### Ship Placement
+ Once the player has selected the number of ships and the size of the board, they can select where they place their ships on the board


### Future Features 

#### Ships bigger than 1 space large
+ The original battleships game has 5 different ships with varying sizes (Aircraft carrier, battleship, cruiser, submariner and + destroyer).
+ The game is played on a 10 * 10 grid and requires all coordinates of a ship to be hit before it sinks. When a player hits a ship, the opponent must announce "Hit", when all the coordinates have been hit the opponent must announce "Hit and sank".

#### Multiplayer Game Mode
+ Initial message would allow player to choose between playing a computer and player.
+ Size and ship number would still be chosen by player. 
+ Ships coordinates would both be randomly generated
+ Both boards would not display ships so that the game can be played.

## Testing

### Bugs

#### Solved Bugs
+ When first creating the function `valid_coordinates()` I duplicated the check for coordinates that had already been entered.
++ I used an `if` check looking throught the guessses list and then another `if ` check looking through the ships.
++ This was providing false Falses as some of the guesses were valid but in the ships list so would return falses.
++ I could avoid this error going forward by planning out functions more methodically. 