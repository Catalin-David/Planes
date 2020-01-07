from os import *
from service import Service

class UI:
    def __init__(self, name):
        self._service = Service(name)
        self._start()

    def _printMenu(self):
        print("This project was made by David Catalin Ioan.\n")
        print("Choose your option:")
        print("1. Play game")
        print("2. Exit")

    def _printPlayers(self):
        string = self._service._getPlayers()
        print(string)

    def _printPlayer1(self):
        string = self._service._getPlayer1()
        print(string)

    def _printMask2(self):
        string = self._service._getMask2()
        print(string)
        
    def _playerView(self):
        self._printPlayer1()
        self._printMask2()

    def _playerMove(self):
        ok = False
        while ok == False:
            move = input("Your move should be of type XY, where X belongs to A-H and Y belongs to 1-8\nEnter your move: ")
            if len(move) != 2 or move[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or move[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                print("Move is not okay")
            else:
                x = ord(move[0])-ord('A')
                y = ord(move[1])-ord('1')
                try:
                    self._service._playerMoves(x, y)
                    ok = True
                except Exception as e:
                    print(e)
        system("cls")

    def _computerMove(self):
        pos = self._service._computerMoves()
        x = chr(pos[0]//8+ord('A'))
        y = chr(pos[0]%8+ord('1'))
        hit_status = ""
        if pos[1] == 1:
            hit_status = " and it hit"
        else:
            hit_status = " and it didn't hit"
        print("Computer moves at " + x + y + hit_status)
    def _play(self):
        self._printPlayer1()
        ok = False
        while ok == False:
            print("Location of first plane should be XY where X belongs to A-H and Y belongs to 1-8")
            p1 = input(">Enter location of first plane: ").strip()
            dire = input("Write direction of first plane: for North write N, for West write W, for East write E and for South write S: ").strip()
            if len(p1) != 2 or p1[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or p1[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"] or dire not in ["N", "W", "E", "S"]:
                print("Position of first plane not okay")
            else:
                x = ord(p1[0])-ord('A')
                y = ord(p1[1])-ord('1')
                d = 0
                if dire == "N":
                    d = 0
                elif dire == "W":
                    d = 1
                elif dire == "E":
                    d = 2
                else:
                    d = 3
                try:
                    self._service._putPlane(x*8+y, d)
                    ok = True
                except:
                    print("Position of first plane not okay")
        self._printPlayer1()
        ok = False
        while ok == False: 
            print("Location of second plane should be XY where X belongs to A-H and Y belongs to 1-8")
            p2 = input(">Enter location of second plane: ").strip()
            dire = input("Write direction of second plane: for North write N, for West write W, for East write E and for South write S: ").strip()
            if len(p2) != 2 or p2[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"] or p2[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"] or dire not in ["N", "W", "E", "S"]:
                print("Position of second plane not okay")
            else:
                x = ord(p2[0])-ord('A')
                y = ord(p2[1])-ord('1')
                d = 0
                if dire == "N":
                    d = 0
                elif dire == "W":
                    d = 1
                elif dire == "E":
                    d = 2
                else:
                    d = 3
                try:
                    self._service._putPlane(x*8+y, d)
                    ok=True
                except:
                    print("Position of second plane not ok")
                    
        system("cls")
        while self._service._getHp1() > 0 and self._service._getHp2() > 0:
            self._playerView()
            self._playerMove()
            if self._service._getHp2() > 0:
                self._computerMove()
        self._playerView()
        if self._service._getHp1() == 0:
            print("You lost!")
        else:
            print("You won!")
    def _start(self):
        while(True):
            try:
                self._printMenu()
                userInput = input(">")
                if userInput == "1":
                    self._play()
                elif userInput == "2":
                    break
                else:
                    print("Invalid command")
            except Exception as e:
                print(e)
            system("pause")
            system("cls")
            self._service = Service(name)