from player import Player
from random import *
import unittest

def generate(cap, dire, board):
    '''
    Function generates a plane on a given board, with a given direction, at some location
    params: cap - head of the plane
            dire - direction of the plane
            board - the board on which we place the plane
    output: - the modified board, if placing the plane was successful
            - the board which was given as input, otherwise
    '''
    newboard = []
    for i in range(0, 64):
        newboard.append(board[i])
    posx = cap//8
    posy = cap%8
    px = [];py=[]
    px.append(posx)
    py.append(posy)
    if dire == 0:
        px.append(posx+1);px.append(posx+1);px.append(posx+1);px.append(posx+1);px.append(posx+1);px.append(posx+2);px.append(posx+3);px.append(posx+3);px.append(posx+3)
        py.append(posy-2);py.append(posy-1);py.append(posy);py.append(posy+1);py.append(posy+2);py.append(posy);py.append(posy-1);py.append(posy);py.append(posy+1)
        
    elif dire == 1:
        px.append(posx-2);px.append(posx-1);px.append(posx);px.append(posx+1);px.append(posx+2);px.append(posx);px.append(posx-1);px.append(posx);px.append(posx+1)
        py.append(posy+1);py.append(posy+1);py.append(posy+1);py.append(posy+1);py.append(posy+1);py.append(posy+2);py.append(posy+3);py.append(posy+3);py.append(posy+3)

    elif dire == 2:
        px.append(posx-2);px.append(posx-1);px.append(posx);px.append(posx+1);px.append(posx+2);px.append(posx);px.append(posx-1);px.append(posx);px.append(posx+1)
        py.append(posy-1);py.append(posy-1);py.append(posy-1);py.append(posy-1);py.append(posy-1);py.append(posy-2);py.append(posy-3);py.append(posy-3);py.append(posy-3)
    
    else:
        px.append(posx-1);px.append(posx-1);px.append(posx-1);px.append(posx-1);px.append(posx-1);px.append(posx-2);px.append(posx-3);px.append(posx-3);px.append(posx-3)
        py.append(posy-2);py.append(posy-1);py.append(posy);py.append(posy+1);py.append(posy+2);py.append(posy);py.append(posy-1);py.append(posy);py.append(posy+1)

    for i in range(0, 10):
        posx = px[i]
        posy = py[i]
        if posx < 0 or posx > 7 or posy < 0 or posy > 7 or board[posx*8+posy] == "1":
            return board
        else:
            newboard[posx*8+posy] = "1"
    
    return newboard

def generateScenarios():
    '''
    Function generates all the possible valid scenarios of a board with 2 planes on it and returns them
    '''
    scenarios = []
    for i in range (0, 64):
        for j in range (0, 64):
            for p1 in range(0, 4):
                board = []
                for k in range(0, 64):
                    board.append("*")
                board1 = generate(i, p1, board)
                if str(board) != str(board1):
                    for p2 in range(0, 4):
                        board2 = generate(j, p2, board1)
                        if str(board2) != str(board1):
                            scenarios.append(board2)
    return scenarios

class Repository:
    def __init__(self, name):
        self._player1 = Player(name)
        self._player2 = Player()
        self._scenarios  = generateScenarios() 
        self._player2.Board = self._scenarios[randint(0,1095)]

    def _getPlayers(self):
        return str(self._player1) + str(self._player2)

    def _getPlayer1(self):
        return str(self._player1)

    def _getPlayer2(self):
        return str(self._player2)

    def _putPlane(self, cap, dire):
        '''
        Function places a plane on the human player's board
        params: cap - head of the plane
                dire - direction of the plane
        '''
        newBoard = generate(cap, dire, self._player1.Board)
        if str(newBoard) == str(self._player1.Board):
            raise ValueError("Could not place plane. Check that is inside the board and does not overlap the other plane")
        else:
            self._player1.Board = newBoard

    def _getHp1(self):
        return self._player1.Hp

    def _getHp2(self):
        return self._player2.Hp

    def _getMask2(self):
        return self._player2._printMask()

    def _playerMoves(self, x, y):
        '''
        Function computes the result of a move made by the human player
        params: x - x coordinate of the move
                y - y coordinate of the move
        '''
        mask = self._player2.Mask
        board = self._player2.Board
        if mask[x*8+y] != '.':
            raise ValueError("Move has already been done")
        else:
            mask[x*8+y] = board[x*8+y]
            if mask[x*8+y] == "1":
                self._player2.Hp -= 1

    def _computerHit(self, x):
        '''
        Function computes the result of a move made by the computer player
        params: x - coordinate of the move
        '''
        board = self._player1.Board
        if board[x] == "1":
            self._player1.Hp -=1
            board[x] = "x"
            return True
        else:
            board[x]="x"
            return False

    @property
    def Board(self):
        return self._player1.Board

    @property
    def Scenarios(self):
        return self._scenarios

class testing_repo(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.test_generate()
        self.test_generateScenarios()

    def test_generate(self):
        board = []
        for i in range(0, 64):
            board.append('*')
        newBoard = generate(0, 0, board)
        self.assertEqual(str(board), str(newBoard))
        newBoard = generate(16, 2, board)
        self.assertEqual(str(board), str(newBoard))
    
    def test_generateScenarios(self):
        scenarios = generateScenarios()
        board = []
        for i in range(0, 64):
            board.append("*")
        board = generate(2, 0, board)
        board = generate(61, 3, board)
        ok = False
        for scenario in scenarios:
            if str(scenario) == str(board):
                ok = True
                break
        self.assertTrue(ok)

        board = []
        for i in range(0, 64):
            board.append("*")

        ok = False
        for scenario in scenarios:
            if str(scenario) == str(board):
                ok = True
                break
        self.assertFalse(ok)

        board = generate(27, 1, board)
        for scenario in scenarios:
            if str(scenario) == str(board):
                ok = True
                break
        self.assertFalse(ok)

        board = generate(58, 3, board)
        for scenario in scenarios:
            if str(scenario) == str(board):
                ok = True
                break
        self.assertTrue(ok)

testing = testing_repo()