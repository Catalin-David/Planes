from repo import Repository
from repo import generate
import unittest

class Service():
    def __init__(self, name):
        self._repository = Repository(name)

    def _getPlayers(self):
        return self._repository._getPlayers()

    def _getPlayer1(self):
        return self._repository._getPlayer1()

    def _getPlayer2(self):
        return self._repository._getPlayer2()

    def _putPlane(self, cap, dire):
        self._repository._putPlane(cap, dire)
    
    def _getHp1(self):
        return self._repository._getHp1()

    def _getHp2(self):
        return self._repository._getHp2()

    def _getMask2(self):
        return self._repository._getMask2()

    def _playerMoves(self, x, y):
        self._repository._playerMoves(x, y)

    def _computerMoves(self):
        '''
        Function generates the most optimal move that can be made by the computer
                and removes scenarios which are impossible after seeing the result of its move 
        output: pos_maxim - position where move was made + 1 (if the move hit)
                                                           0 (if the move did not hit)
        '''
        board = self._repository.Board
        scenarios = self._repository.Scenarios
        chances = []
        for i in range(0, 64):
            chances.append(0)
        for scenario in scenarios:
            for i in range(0,64):
                if scenario[i] == "1" and board[i] != "x":
                    chances[i] += 1
        maxim = 0
        pos_maxim = -1
        for i in range(0, 64):
            if chances[i] > maxim:
                maxim = chances[i]
                pos_maxim = i
        if self._repository._computerHit(pos_maxim):
            i = 0
            while i < len(scenarios):
                scenario = scenarios[i]
                if scenario[pos_maxim] == "*":
                    scenarios.remove(scenario)
                    i -= 1
                i += 1
            return [pos_maxim, 1]
        else:
            i = 0
            while i < len(scenarios):
                scenario = scenarios[i]
                if scenario[pos_maxim] == "1":
                    scenarios.remove(scenario)
                    i -= 1
                i += 1  
            return [pos_maxim, 0]

class testing_service(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self._service = Service("David")
        self.test_computerMoves()

    def test_computerMoves(self):
        self._service._repository.Scenarios.clear()
        board = []
        for i in range(0,64):
            board.append("*")
        board = generate(61, 3, board)
        board1 = generate(2, 0, board)
        board2 = generate(5, 0, board)
        self._service._repository._scenarios.append(board1)
        self._service._repository._scenarios.append(board2)
        self.assertEqual([11, 0], self._service._computerMoves())

testing = testing_service()