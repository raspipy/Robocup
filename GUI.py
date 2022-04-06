from tkinter import *

class GUI(Tk):
    def __init__(self):
        self.__init__()
        self.title("Raspberrypi Robot Tester")
        self.geometry("500x500")
        self.resizable(0,0)
        self.configure(background="white")
        self.__create_widgets()

if __name__ == "__main__":
    GUI()