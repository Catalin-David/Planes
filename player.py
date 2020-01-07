class Player:
    def __init__(self, name = "Computer"):
        self._hp = 20
        self._name = name
        self._board = []
        for i in range(0, 64):
            self._board.append("*")
        self._mask = []
        for i in range(0, 64):
            self._mask.append('.')

    @property
    def Hp(self):
        return self._hp

    @Hp.setter
    def Hp(self, value):
        self._hp = value

    @property
    def Board(self):
        return self._board

    @Board.setter
    def Board(self, value):
        self._board = value

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def Mask(self):
        return self._mask

    @Mask.setter
    def Mask(self, value):
        self._mask = value

    def __str__(self):
        numbers = "  1 2 3 4 5 6 7 8\n"
        letters="ABCDEFGH"
        string = "\n" + self._name + ":\n" + numbers
        for i in range(0, 8):
            string = string + letters[i] + " "
            for j in range(0, 8):
                string = string + self._board[i*8+j] + " "
            string = string + letters[i] + "\n"
        string = string + numbers
        string = string + "This player's HP is " + str(self._hp) + "\n"
        return string

    def _printMask(self):
        '''
        Function returns a string which contains the mask of a player
        '''
        numbers = "  1 2 3 4 5 6 7 8\n"
        letters="ABCDEFGH"
        string = "\n" + self._name + ":\n" + numbers
        for i in range(0, 8):
            string = string + letters[i] + " "
            for j in range(0, 8):
                string = string + self._mask[i*8+j] + " "
            string = string + letters[i] + "\n"
        string = string + numbers
        string = string + "This player's HP is " + str(self._hp) + "\n"
        return string
