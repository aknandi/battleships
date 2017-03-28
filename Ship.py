class Ship:
    def __init__(self, start_position, end_position):
        self.start_position = start_position
        self.end_position = end_position
        self.hits = 0
        
    def __get_startrow(self):
        return self.start_position[0]
        
    def __get_startcolumn(self):
        return self.start_position[1]

    def __get_endrow(self):
        return self.end_position[0]
        
    def __get_endcolumn(self):
        return self.end_position[1]

    def get_length(self):
        if self.__get_startrow() == self.__get_endrow():
            return abs(self.__get_startcolumn() - self.__get_endcolumn()) + 1
        else:
            return abs(self.__get_startrow() - self.__get_endrow()) + 1

    def __get_all_occupied_spaces(self):
        self.occupied_spaces = []
        if self.__get_startrow() == self.__get_endrow():
            row = self.__get_startrow()
            length = abs(self.__get_startcolumn() - self.__get_endcolumn())
            for i in range(0,length+1):
                self.occupied_spaces.append([row,min(self.__get_startcolumn(),self.__get_endcolumn())+i])
        else:
            column = self.__get_startcolumn()
            length = abs(self.__get_startrow() - self.__get_endrow())
            for i in range(0,length+1):
                self.occupied_spaces.append([min(self.__get_startrow(),self.__get_endrow())+i,column])
        return self.occupied_spaces
        
    def is_occupying_position(self, position):
        self.occupied_spaces = self.__get_all_occupied_spaces()
        for space in self.occupied_spaces:
            if position[0] == space[0] and position[1] == space[1]:
                return True
        return False
        
    def is_touching(self, otherShip):
        self.occupied_spaces1 = self.__get_all_occupied_spaces()
        self.occupied_spaces2 = otherShip.__get_all_occupied_spaces()
        for space1 in self.occupied_spaces1:
            for space2 in self.occupied_spaces2:
                if abs(space1[0]-space2[0]) <= 1 and abs(space1[1]-space2[1]) <= 1:
                    return True
        return False
            
    def __eq__(self, other):
        return (self.start_position == other.start_position and self.end_position == other.end_position) or (self.start_position == other.end_position and self.end_position == other.start_position)
        
    def __repr__(self):
        return "(" + str(self.__get_startrow()) + "," + str(self.__get_startcolumn()) + " to " + str(self.__get_endrow()) + "," + str(self.__get_endcolumn()) + ")"
