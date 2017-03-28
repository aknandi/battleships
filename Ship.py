from random import randint

class Ship:
    def __init__(self, position):
        self.position = position
        
    def __get_row(self):
        return self.position[0]
        
    def __get_column(self):
        return self.position[1]
        
    def is_occupying_position(self, position):
        return self.__get_row() == position[0] and self.__get_column() == position[1]
        
    def is_touching(self, otherShip):
        if ((abs(self.__get_row()-otherShip.__get_row()) <= 1)
            and (abs(self.__get_column()-otherShip.__get_column()) <= 1)):
            return True
        else:
            return False
            
    def __eq__(self, other):
        return self.position == other.position
        
    def __repr__(self):
        return "(" + str(self.__get_row()) + ", " + str(self.__get_column()) + ")"
