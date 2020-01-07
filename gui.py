from service import Service
from tkinter import *


class GUI:

    def __init__(self, master, name):
        self.master = master
        self.service = Service(name)
        master.title("Planes")

        self.canvas = Canvas(master, height = 675, width = 1200)
        self.backgroundImage = PhotoImage(file='background.png')
        self.backgroundLabel = Label(master, image = self.backgroundImage)

        self.newGameButton = Button(master, text = "Start new game", command = lambda: self.newGame(name))
        self.quitGameButton = Button(master, text = "Quit game", command = master.destroy)

        self.labelPlayer1 = Label(master, font = 50, text = "This is player1's board")
        self.labelPlayer2 = Label(master, font = 50, text = "This is player2's mask")

        # LAYOUT

        self.canvas.pack()
        self.backgroundLabel.place(relheight = 1, relwidth = 1)
        self.newGameButton.place(relwidth = 0.75*0.2, relheight = 0.75*0.1)
        self.quitGameButton.place(rely = 0.75*0.1, relwidth = 0.75*0.2, relheight = 0.75*0.1)
        self.labelPlayer1.place(rely = 0.3, relheight = 0.4, relx = 0.2, relwidth = 0.25)
        self.labelPlayer2.place(rely = 0.3, relheight = 0.4, relx = 0.55, relwidth = 0.25)

        self.play()

    def newGame(self, name):
        self.service = Service(name)
        self.play()

    def printPlayer1(self):
        string = self.service._getPlayer1()
        self.labelPlayer1['text'] = string

    def playerView(self):
        string = self.service._getPlayer1()
        self.labelPlayer1['text'] = string
        string = self.service._getMask2()
        self.labelPlayer2['text'] = string

    def play(self):
        self.playerView()
'''
def startGUI(name):

    root = Tk()

    Canvas(root, height = 675, width = 1200).pack()
    Label(root, image = PhotoImage(file = 'background.png')).place(relheight = 1, relwidth = 1)      


    Button(root, text = "Start new game", font = 40, command = newGame()).place(relwidth = 0.75*0.2, relheight = 0.75*0.1)
    Button(root, text = "Quit game", font = 40, command = root.destroy).place(rely = 0.75*0.1, relwidth = 0.75*0.2, relheight = 0.75*0.1)

    root.mainloop()
'''