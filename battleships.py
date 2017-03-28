"""
Possible Extensions:
 Different size battleships
 Two player game
 Rematches and statistics
"""
from random import randint
from Board import Board
from Ship import Ship

def generate_ship_position(dim):
    ship_row = randint(0,dimension - 1)
    ship_column = randint(0,dimension - 1)
    position = [ship_row,ship_column]
    return Ship(position)

def can_add_ship(new_ship):
    for current_ship in ship_positions:
        if current_ship.is_touching(new_ship):
            return False
    return True

def ship_hit(guess):
    for ship in ship_positions:
        if ship.is_occupying_position(guess):
            return True
    return False

dimension = 4
number_of_turns = 4
number_of_ships = 4
board = Board(dimension)
print board

ship_positions = []
for i in range(number_of_ships):
    new_ship = generate_ship_position(dimension)
    while (not can_add_ship(new_ship)):
        new_ship = generate_ship_position(dimension)
    ship_positions.append(new_ship)

print "There are", number_of_ships, "battleships"
print ship_positions
turn = 0
while turn < number_of_turns:
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row (0 to "+str(dimension - 1)+"): "))
    guess_column = int(raw_input("Guess Column (0 to "+str(dimension - 1)+"): "))
    guess_position = [guess_row,guess_column]
    
    if not board.has_position(guess_position):
        print "Oops, that's not even in the ocean"
    elif (board.get_cell(guess_position) == "X" or board.get_cell(guess_position) == "-"):
        print "You guessed that one already"
    elif ship_hit(guess_position):
        print "Congratulations! You sunk a battleship!"
        number_of_turns += 1
        board.set_cell(guess_position,"X")
        ship_positions.remove(Ship([guess_row,guess_column]))
        if ship_positions == []:
            print "You have sunk all the battleships!"
            break
    else:
        print "You missed my battleships!"
        board.set_cell(guess_position,"-")
    print board
    turn += 1

if len(ship_positions) > 0:
    print "Game Over :("
