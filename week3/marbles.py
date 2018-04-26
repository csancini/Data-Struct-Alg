class MarblesBoard:

    def __init__(self, play):
        self.__play = list(play)

    def switch(self):
        a = self.__play[1]
        self.__play[1] = self.__play[0]
        self.__play[0] = a

    def rotate(self):
        temp = self.__play[1:]
        temp.append(self.__play[0])
        self.__play = temp

    def is_solved(self):
        ordered = True
        for i in range(len(self.__play)-1):
            ordered &= (self.__play[i] < self.__play[i+1])
        return ordered

    def __repr__(self):
        self.__str__()

    def __str__(self):
        return " ".join(str(m) for m in self.__play)


board = MarblesBoard((3, 6, 7, 4, 1, 0, 8, 2, 5))
print(board)
board.switch()
print(board)
board.rotate()
print(board)


print(board.is_solved())