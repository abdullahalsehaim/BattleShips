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
        self.board = []
        self.ship_num = ship_num
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(" ".join(row))
    
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
    Returns a random integer between 0 and size
    """
    return randint(0, size -1)


def valid_coordinates(x, y, board):
    """
    Ensure coorindate is an actual location on the board, 
    also has not already been selected by user.
    """
    
    if  0 > (x or y) > 4:
        print("Value must be between 0 and 4")


def populate_board(board):


def make_guess(board):


def play_game(computer_board, player_board):


def new_game():
    """
    Begins a new game. Establishes size of board, number of ships, 
    sets scores to 0, and randomly assigns boats.
    """

    size = 5
    ship_num = 4
    scores["computer"] = 0
    scores["player"] = 0

    computer_board = Board(size, ship_num, "Computer", type="computer")
    player_board = Board(size, ship_num, player_name, type="player")

    for _ in range(ship_num):
        populate_board(player_board)
        populate_board(computer_board)


