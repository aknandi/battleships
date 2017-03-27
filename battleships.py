"""
Possible Extensions:
 Multiple battleships
 Different size battleships
 Two player game
 Rematches and statistics
"""
from random import randint

def initialise_board(dim):
    board = []
    for i in range(dim):
        board.append(["O"]*dim)
    return board

def print_board(board):
    for row in board:
        print " ".join(row)

def generate_ship_position(dim):
    ship_row = randint(0,dimension - 1)
    ship_column = randint(0,dimension - 1)
    return [ship_row,ship_column]

def valid_ship_position(new_ship_position):
    count = 0
    is_valid = True
    for current_ship in ship_positions:
        is_valid = compare(current_ship,new_ship_position)
        if (not is_valid):
            return is_valid
    return is_valid

def compare(ship1,ship2):
    if (abs(ship1[0]-ship2[0]) <= 1) and (abs(ship1[1]-ship2[1]) <= 1):
        return False
    else:
        return True

def ship_hit(guess):
    for ship in ship_positions:
        if ship[0]==guess[0] and ship[1]==guess[1]:
            return True
    return False

dimension = 5
number_of_turns = 4
number_of_ships = 4
board = initialise_board(dimension)
print_board(board)
ship_positions = []
for i in range(number_of_ships):
    new_ship = generate_ship_position(dimension)
    while (not valid_ship_position(new_ship)):
        new_ship = generate_ship_position(dimension)
    ship_positions.append(new_ship)

turn = 0
while turn < number_of_turns:
#for turn in range(number_of_turns):
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row: "))
    guess_column = int(raw_input("Guess Column: "))
    guess_position = [guess_row,guess_column]
    if ship_hit(guess_position):
        print "Congratulations! You sunk a battleship!"
        number_of_turns += 1
        board[guess_row][guess_column] = "X"
        ship_positions.remove([guess_row,guess_column])
        if ship_positions == []:
            print "You have sunk all the battleships!"
            break
    else:
        if (guess_row < 0 or guess_row > dimension - 1) or (guess_column < 0 or guess_column > dimension - 1):
            print "Oops, that's not even in the ocean"
        elif (board[guess_row][guess_column] == "X" or board[guess_row][guess_column] == "-"):
            print "You guessed that one already"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_column] = "-"
    print_board(board)
    turn += 1

print "Game Over :("
