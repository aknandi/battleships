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

dimension = 5
number_of_turns = 4
board = initialise_board(dimension)
print_board(board)
ship_row = randint(0,dimension - 1)
ship_column = randint(0,dimension - 1)

for turn in range(number_of_turns):
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row: "))
    guess_column = int(raw_input("Guess Column: "))
    if guess_row == ship_row and guess_column == ship_column:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > dimension - 1) or (guess_column < 0 or guess_column > dimension - 1):
            print "Oops, that's not even in the ocean"
        elif (board[guess_row][guess_column] == "X"):
            print "You guessed that one already"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_column] = "X"
    print_board(board)
    if turn == number_of_turns - 1:
        print "Game Over :("
