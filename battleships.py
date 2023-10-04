"""
Possible Extensions:
 Two player game
 Rematches and statistics
"""
from random import randint
from Board import Board
from Ship import Ship
import sys

def generate_ship(dimension,length):
    ship_row = randint(0,dimension - 1)
    ship_column = randint(0,dimension - 1)
    start_position = [ship_row,ship_column]
    end_position = start_position
    direction = randint(0,3)
    if direction==0: # right
        end_position = [ship_row,ship_column+length-1]
    elif direction==1: # up
        end_position = [ship_row-(length-1),ship_column]
    elif direction==2: # left
        end_position = [ship_row,ship_column-(length-1)]
    elif direction==3: # down
        end_position = [ship_row+length-1,ship_column]
    board = Board(dimension)
    if board.has_position(end_position):
        return Ship(start_position,end_position)
    else:
        ship = generate_ship(dimension,length)
        return ship

def get_position_from_user_input(guess_space):
    guess_row = board.letters.index(guess_space[0])
    guess_column = int(guess_space[1])
    return [guess_row,guess_column]

def can_add_ship(new_ship):
    for current_ship in ship_positions:
        if current_ship.is_touching(new_ship):
            return False
    return True

def is_ship_hit(guess):
    return get_ship_hit(guess) is not None

def get_ship_hit(guess):
    for ship in ship_positions:
        if ship.is_occupying_position(guess):
            return ship
    return None

dimension = 5
number_of_turns = 4
# An element of [m,n] means m battleships of size n
initial_ships = [[0,5],[0,4],[1,3],[1,2],[3,1]]
board = Board(dimension)
print(board)

ship_positions = []
for number_of_ships,size_of_ship in initial_ships:
    for i in range(number_of_ships):
        count = 0
        new_ship = generate_ship(dimension,size_of_ship)
        while (not can_add_ship(new_ship)):
            count += 1
            if count > 10:
                print("Cannot fit battleships on board. Try running again or reduce the number of battleships\n")
                sys.exit()
            new_ship = generate_ship(dimension,size_of_ship)
        ship_positions.append(new_ship)

print("There are:")
for number_of_ships,size_of_ship in initial_ships:
    print("\t" + str(number_of_ships) + " battleships of size " + str(size_of_ship))

#print ship_positions
turn = 0
while turn < number_of_turns:
    print("Turn", turn+1)
    guess_space = input("Guess position (e.g. A0) : ")
    guess_position = get_position_from_user_input(guess_space)    
    if not board.has_position(guess_position):
        print("Oops, that's not even in the ocean")
    elif (board.get_cell(guess_position) == "X" or board.get_cell(guess_position) == "-"):
        print("You guessed that one already")
    elif is_ship_hit(guess_position):
        print("Congratulations! You hit a battleship!")
        number_of_turns += 1
        board.set_cell(guess_position,"X")
        ship_hit = get_ship_hit(guess_position)
        ship_hit.hits += 1
        if ship_hit.hits == ship_hit.get_length():
            ship_positions.remove(ship_hit)
            print("Congratulations! You sunk a whole battleship!")
        if ship_positions == []:
            print(board)
            print("You have sunk all the battleships!")
            break
    else:
        print("You missed my battleships!")
        board.set_cell(guess_position,"-")
    print(board)
    turn += 1

if len(ship_positions) > 0:
    print("Game Over :(")
