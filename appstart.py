from tkinter import *
from gui import GUI
from ui import UI

name = input("Enter your name here: ")
uiTYPE = input("Which type of UI would you like(c -> console; g -> gui): ")
if uiTYPE == "c":
    ui = UI(name)
elif uiTYPE == "g":
    root = Tk()
    my_gui = GUI(root, name)
    root.mainloop()
else:
    print("If you can't even choose between c and g, I feel bad for you ;)")
