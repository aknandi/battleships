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
