class Board():
    
   def __init__(self, dimension):
       self.dimension = dimension
       self.board = []
       for i in range(dimension):
           self.board.append(["O"]*dimension)
    
   def get_cell(self, position):
       return self.board[position[0]][position[1]]
        
   def set_cell(self, position, value):
       self.board[position[0]][position[1]] = value
   
   def has_position(self, position):
       return (position[0] >= 0 and position[0] <= self.dimension - 1
           and position[1] >= 0 and position[1] <= self.dimension - 1)
   
   def __str__(self):
       output = "  " + " ".join([str(x) for x in range(0,self.dimension)]) + "\n"
       row_number = 0
       for row in self.board:
           output += str(row_number) + " " + " ".join(row) + "\n"
           row_number += 1
       return output
