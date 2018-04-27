import sys


class MarblesBoard:
    """
    Implements a the marbles game board.
    """

    def __init__(self, play):
        """
        Class initializer that takes the marbles in a random order.
        :param play: a list of integers representing the marbles from position 0 to N-1
        """
        self.__play = list(play)

    def switch(self):
        """
        Executes a switch operation between marbles in the first and second positions.
        :return: None
        """
        tmp = self.__play[1]
        self.__play[1] = self.__play[0]
        self.__play[0] = tmp

    def rotate(self):
        """
        Executes a rotate operation that moves the marble in position 0 to N-1 and move
        all other marbles one space to the left.
        :return: None
        """
        tmp = self.__play[1:]
        tmp.append(self.__play[0])
        self.__play = tmp

    def is_solved(self):
        """
        Evaluates if the marbles are ordered and the game is solved.
        :return: True if the game is solved, False otherwise.
        """
        ordered = True
        for i in range(len(self.__play)-1):
            ordered &= (self.__play[i] < self.__play[i+1])
        return ordered

    def get_first(self):
        """
        Return the marble in position 0.
        """
        return self.__play[0]

    def get_second(self):
        """
        Return the marble in position 1.
        """
        return self.__play[1]

    def __repr__(self):
        self.__str__()

    def __str__(self):
        return " ".join(str(m) for m in self.__play)


class Solver:
    """
    Solves a given marble board.
    """

    def __init__(self, marbles_board: MarblesBoard):
        """Initializes the Solver receiving a MarbleBoard"""
        self.__marbles_board = marbles_board

    def solve(self):
        """
        Solves the marbles games. In each iteration of the game the board is printed.
        When the game is solved, printed the number of steps taken to complete the game.
        """
        steps = 0

        while not self.__marbles_board.is_solved():
            steps += 1
            print(self.__marbles_board)

            if self.__marbles_board.get_first() == 0 or self.__marbles_board.get_second() == 0:
                self.__marbles_board.rotate()
            elif self.__marbles_board.get_first() > self.__marbles_board.get_second():
                self.__marbles_board.switch()
            else:
                self.__marbles_board.rotate()

        print(self.__marbles_board)
        return print("total steps:", steps)

    def get_board(self):
        """Returns the marble board."""
        return self.__marbles_board


marbles = [int(sys.argv[i][0]) for i in range(1, len(sys.argv))]
board = MarblesBoard(marbles)
solver = Solver(board)
solver.solve()

# The complexity to solve the game is O(n**2): n switches x n rotations
