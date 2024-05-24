from random import randint

scores = {"computer": 0, "user": 0}

class Game:
    """
    The class which will set up our game. 
    This sets the size of the board, number of ships, players name,
    board type. Able to add ships and guesses and prints the game board.
    """
    def __init__(self, size, ship_num, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.ship_num = ship_num
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    #Removes quotation marks and stacks rows
    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    #Appends a guess into the guesses list
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
    

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.ship_num:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Returns a random integer between 0 and size.
    This will be used for the computers guesses.
    """
    #Using randint to generate a number between 0 and the size of the board minus 1(Due to indexing)
    return randint(0, size -1)


def valid_coordinates(x, y, board):
    """
    Ensure coorindate is an actual location on the board, 
    also has not already been selected by user.
    """
    #Checks if coordinate is within boundaries of the board
    if not (0 <= x < self.size and 0 <= y < self.size):
        print("Value must be between 0 and 4")
        return False
    
    #Checks if the coordinate has already been selected and added to the guesses 
    if (x, y) in self.guesses:
        print("Coordinate has already been selected, please choose another")
        return False
    
    #In this game format ships only take one hit to sink,
    #previous coordinates cannot be valid
    #Check if spot is already occupied by another ship
    return (x, y) not in self.ships
    


def populate_board(board):
    """
    Creates random ship placement for both user and computer
    """
    



def make_guess(board):
    """
    Prompts user to input their guess, computer's guess is randomly generated
    using previously defined random point function.
    """
    if board == "player":
        row_guess = input("Enter a row:\n")
        col_guess = input("Enter a column:\n")
        user_guess = (row_guess, col_guess)
        return user_guess
    elif board == "computer":
        cpu_guess = (random_point(size), random_point(size))
        return cpu_guess



    

    




def play_game(computer_board, player_board):
    """
    Establishes each new round of play. Continues until user or CPU 
    reaches a score of 4
    """


def new_game():
    """
    Begins a new game. Establishes size of board, number of ships, 
    sets scores to 0, and randomly assigns boats.
    """

    size = 5
    ship_num = 4
    scores["computer"] = 0
    scores["player"] = 0


    player_name = input("Please enter your name: ")

    computer_board = Game(size, ship_num, "Computer", type="computer")
    player_board = Game(size, ship_num, player_name, type="player")

    for _ in range(ship_num):
        populate_board(player_board)
        populate_board(computer_board)


