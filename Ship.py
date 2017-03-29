class Ship:
    def __init__(self, start_position, end_position):
        self.__start_position = start_position
        self.__end_position = end_position
        self.hits = 0
        self.__length = self.__calculate_length()
        self.__occupied_spaces = self.__calculate_all_occupied_spaces()
        
    def __get_startrow(self):
        return self.__start_position[0]
        
    def __get_startcolumn(self):
        return self.__start_position[1]

    def __get_endrow(self):
        return self.__end_position[0]
        
    def __get_endcolumn(self):
        return self.__end_position[1]

    def __calculate_length(self):
        if self.__get_startrow() == self.__get_endrow():
            return abs(self.__get_startcolumn() - self.__get_endcolumn()) + 1
        else:
            return abs(self.__get_startrow() - self.__get_endrow()) + 1

    def __calculate_all_occupied_spaces(self):
        occupied_spaces = []
        if self.__get_startrow() == self.__get_endrow():
            row = self.__get_startrow()
            for i in range(0,self.__length):
                occupied_spaces.append([row,min(self.__get_startcolumn(),self.__get_endcolumn())+i])
        else:
            column = self.__get_startcolumn()
            for i in range(0,self.__length):
                occupied_spaces.append([min(self.__get_startrow(),self.__get_endrow())+i,column])
        return occupied_spaces

    def get_length(self):
        return self.__length
 
    def is_occupying_position(self, position):
        for space in self.__occupied_spaces:
            if position[0] == space[0] and position[1] == space[1]:
                return True
        return False
        
    def is_touching(self, otherShip):
        for space1 in self.__occupied_spaces:
            for space2 in otherShip.__occupied_spaces:
                if abs(space1[0]-space2[0]) <= 1 and abs(space1[1]-space2[1]) <= 1:
                    return True
        return False
            
    def __eq__(self, other):
        return ((self.__start_position == other.__start_position and self.__end_position == other.__end_position)
            or (self.__start_position == other.__end_position and self.__end_position == other.__start_position))
        
    def __repr__(self):
        return "(" + str(self.__get_startrow()) + "," + str(self.__get_startcolumn()) + " to " + str(self.__get_endrow()) + "," + str(self.__get_endcolumn()) + ")"
