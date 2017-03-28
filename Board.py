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
       output = ""
       for row in self.board:
           output += " ".join(row) + "\n"
       return output
