from random import randint


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
        self.player_guesses = []
        self.computer_guesses = []
        self.ships = []

    # Removes quotation marks and stacks rows
    def print(self):
        for row in self.board:
            print(" ".join(row))

    # Appends a guess into the guesses list
    def guess(self, x, y):
        if self.type == "player":
            self.player_guesses.append((x, y))
            self.board[x][y] = "X"

        elif self.type == "computer":
            self.computer_guesses.append((x, y))
            self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    # Adds ship coordinates to list

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
    # Using randint to generate a number between 0
    # and the size of the board minus 1
    # (Due to indexing)
    return randint(0, size - 1)


def valid_coordinates(x, y, board, computer_board, player_board):
    """
    Ensure coorindate is an actual location on the board,
    has not already been selected by user and rejects non-numeric input.
    """
    # Checks if coordinate is within boundaries of the board
    if not 0 <= x < board.size or not 0 <= y < board.size:
        print("Value must be between 0 and", board.size-1)
        return False

    # Checks if the coordinate has already been selected
    if board.type == "player":
        if (x, y) in computer_board.computer_guesses:
            print("You already guessed this coordinate, please pick another.")
            return False

    if board.type == "computer":
        if (x, y) in player_board.player_guesses:
            return False

    # If all above checks have passed, the coordinate is valid so returns true
    return True


def valid_ship(x, y, board):
    """
    Ensures user ship placement is within the boundaries of the board
    and no two ships are placed in the same coordinate.
    """
    # Checks if coordinate is within boundaries of the board
    if not 0 <= x < board.size or not 0 <= y < board.size:
        print("Value must be between 0 and", board.size-1)
        return False

    # Checks if this position has already been selected
    if (x, y) in board.ships:
        print("You have already guessed this coordinate, please pick another.")
        return False

    # If ship coordinates pass other two checks returns true
    return True


def valid_size():
    """
    Prompts player to choose the size of the board,
    will check if the size is valid
    """
    while True:
        try:
            size = int(input("Enter the board size (between 4 and 8):\n"))
            if 4 <= size <= 8:
                return size
            else:
                print("Error: Please enter a size between 4 and 8(inclusive).")
        except ValueError:
            print("Error please enter an integer")


def valid_num():
    """
    Prompts user to select number of ships, checks if input is valid.
    """
    while True:
        try:
            ship_num = int(input("Enter number of ships between 2 and 6:\n"))
            if 2 <= ship_num <= 6:
                return ship_num
            else:
                print("Error: Enter a ship number between 2 and 6(inclusive).")
        except ValueError:
            print("Error please enter an integer")


def populate_board(board):
    """
    This function puts ships on the board.
    Prompts user to place thier ships on the board.
    Computers ships will be randomly generated.
    Users ships will be visible in the terminal, computers will not be.
    """
    if board.type == "player":
        place_ship = get_ship_placement(board)
        board.add_ship(place_ship[0], place_ship[1], type)
        print("Player coordinate has been added")

    if board.type == "computer":
        while True:
            new_ship = (random_point(board.size), random_point(board.size))
            if (new_ship[0], new_ship[1]) not in board.ships:
                board.add_ship(new_ship[0], new_ship[1], type)
                break


def get_ship_placement(board):
    """
    Prompts user to choose their ship placement on the board
    """
    while True:
        try:
            ship_row = int(input("Enter a row for your ship\n"))
            ship_col = int(input("Enter a column for your ship\n"))
            if valid_ship(ship_row, ship_col, board):
                return (ship_row, ship_col)
        except ValueError:
            print("Error: Input must be a number")


def make_guess(board, computer_board, player_board):
    """
    Prompts user to input their guess, computer's guess is randomly generated
    using previously defined random point function.
    """
    if board.type == "player":
        while True:
            try:
                row_guess = int(input("Enter a row:\n"))
                col_guess = int(input("Enter a column:\n"))
                if valid_coordinates(row_guess, col_guess, board,
                                     computer_board, player_board):
                    return (row_guess, col_guess)
            except ValueError:
                print("Error: Input must be a number")

    if board.type == "computer":

        while True:
            cpu_guess = (random_point(board.size), random_point(board.size))
            if valid_coordinates(cpu_guess[0], cpu_guess[1],
                                 board, computer_board, player_board):
                return cpu_guess


def play_game(computer_board, player_board, computer_score, player_score):
    """
    Establishes each new round of play. Continues until user or CPU
    reaches a score of ship_num (meaning all ships are sunk)
    """
    while (player_score or computer_score) < player_board.ship_num:

        print(f"{player_board.name}'s Board")
        player_board.print()

        print(f"{computer_board.name}'s Board")
        computer_board.print()

        player_guess = make_guess(player_board, computer_board, player_board)
        print(f"Player guessed: {player_guess}")
        if computer_board.guess(player_guess[0], player_guess[1]) == "Hit":
            print("Player hit this time.")
            player_score += 1
        elif computer_board.guess(player_guess[0], player_guess[1]) == "Miss":
            print("Player missed this time.")

        computer_guess = make_guess(computer_board,
                                    computer_board, player_board)
        print(f"Computer guessed: {computer_guess}")
        if player_board.guess(computer_guess[0], computer_guess[1]) == "Hit":
            print("Computer hit this time.")
            computer_score += 1
        elif player_board.guess(computer_guess[0],
                                computer_guess[1]) == "Miss":
            print("Computer missed this time.")

        print("After this round, the scores are:")
        print(f"{player_board.name}: {player_score}")
        print(f"Computer: {computer_score}")

        continue_game = input("Press any key to continue, press f to quit:\n")
        if continue_game == "f":
            break

    # Check for winners after loop based on ship count sunk
    if player_score == computer_board.ship_num:
        print("GAME OVER")
        print(f"{player_board.name} wins! Congratulations")
    elif computer_score == player_board.ship_num:
        print("GAME OVER")
        print("Computer wins, better luck next time!")

    print("=" * 35)
    start_new_game = input("Enter any key to start a new game\n")


def new_game():
    """
    Begins a new game. Establishes size of board, number of ships,
    sets scores to 0, and randomly assigns boats.
    """
    computer_score = 0
    player_score = 0
    print("=" * 35)
    print("Welcome to BATTLESHIPS GAME!")
    player_name = input("Please enter your name:\n")
    print(f"Welcome {player_name}, please select the size of the board")
    print("and how many ships each player will have.\n")
    size = valid_size()
    print("Board size confirmed.\n")
    ship_num = valid_num()
    print(f"The Board size is {size} X {size}.")
    print(f"Player and Computer have {ship_num} ships each.\n")
    print(f"Top left coorindate is (0, 0)")
    print(f"bottom right coordinate is ({size-1}, {size-1})\n")
    print("=" * 35)
    print("=" * 35)

    computer_board = Game(size, ship_num, "Computer", type="computer")
    player_board = Game(size, ship_num, player_name, type="player")

    print(f"Number of ships is {ship_num}")
    print(f"please now select {ship_num} coordinates.")
    print("=" * 35)

    for _ in range(ship_num):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board, computer_score, player_score)


new_game()
