"""
Possible Extensions:
 Multiple battleships
 Different size battleships
 Two player game
 Rematches and statistics
"""
from random import randint

class Ship:
    def __init__(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position
        
    def getRow(self):
        return self.position[0]
        
    def getColumn(self):
        return self.position[1]
        
    def isOccupyingPosition(self, position):
        return self.getRow() == position[0] and self.getColumn() == position[1]
        
    def isTouching(self, otherShip):
        if ((abs(self.getRow()-otherShip.getRow()) <= 1)
            and (abs(self.getColumn()-otherShip.getColumn()) <= 1)):
            return True
        else:
            return False
            
    def __eq__(self, other):
        return self.getPosition() == other.getPosition()
        
    def __repr__(self):
        return "(" + str(self.getRow()) + ", " + str(self.getColumn()) + ")"

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
    position = [ship_row,ship_column]
    return Ship(position)

def can_add_ship(new_ship):
    for current_ship in ship_positions:
        if current_ship.isTouching(new_ship):
            return False
    return True

def ship_hit(guess):
    for ship in ship_positions:
        if ship.isOccupyingPosition(guess):
            return True
    return False

dimension = 4
number_of_turns = 4
number_of_ships = 4
board = initialise_board(dimension)
print_board(board)
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
    
    if (guess_row < 0 or guess_row > dimension - 1) or (guess_column < 0 or guess_column > dimension - 1):
        print "Oops, that's not even in the ocean"
    elif (board[guess_row][guess_column] == "X" or board[guess_row][guess_column] == "-"):
        print "You guessed that one already"
    elif ship_hit(guess_position):
        print "Congratulations! You sunk a battleship!"
        number_of_turns += 1
        board[guess_row][guess_column] = "X"
        ship_positions.remove(Ship([guess_row,guess_column]))
        if ship_positions == []:
            print "You have sunk all the battleships!"
            break
    else:
        print "You missed my battleships!"
        board[guess_row][guess_column] = "-"
    print_board(board)
    turn += 1

print "Game Over :("
