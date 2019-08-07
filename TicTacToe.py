import numpy as np
from math import floor
from tkinter import Tk, Canvas, Text, INSERT, Frame, Button, ttk, END

class TicTacToe:

    def __init__(self, players, board_size, font_size):
        self.board = np.zeros((board_size, board_size), dtype=str)
        self.printBoard()
        self.players = players
        self.player_index = 0
        self.game_end = False
        self.font_size = font_size

        root = Tk()
        self.master = root
        self.board_size = board_size
        self.initGUI(root)
        root.mainloop()

    def initGUI(self, master):
        self.canvas_height = 500
        self.canvas_width = 500
        self.line_thickness = 5

        master.title("PyTicTacToe")
        master.resizable(False, False)

        self.masterdow_height = 500
        self.masterdow_width = 1000

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (self.masterdow_width / 2))
        y_cordinate = int((screen_height / 2) - (self.masterdow_height / 2))

        master.geometry("{}x{}+{}+{}".format(self.masterdow_width, self.masterdow_height, x_cordinate, y_cordinate))


        self.f = Frame(master)
        self.f.place(relx = 0.5, rely = 0.5, anchor = "w")
        self.t = Text(self.f, width=40, height=1, font=("Helvetica", 32))
        self.b = ttk.Button(self.f, text='Play again', width=15, command=lambda: self.reset())
        self.c = Canvas(master, height=self.canvas_height, width=self.canvas_width, bg="grey", bd = 0)
        master.bind("<Button 1>", self.getorigin)
        self.c.place(relx = 0.5, rely = 0.5, anchor = "e")

        self.drawBoard()

    def move(self, x, y, player):
        self.board[x][y] = player
        self.printBoard()

    def printBoard(self):
        print(np.array_str(self.board))

    def checkEnd(self):
        for i in range(0,3):
            if len(set(self.board[i]))==1 and not self.board[i][0] == '':
                self.game_end = True
                break
            elif len(set(self.board[:, i]))==1 and not self.board[:, i][0] == '':
                self.game_end =  True
                break
            else:
                self.game_end =  False

        if len(set(np.diagonal(self.board)))==1 and not np.diagonal(self.board)[0] == '':
            self.game_end = True
        if len(set(np.fliplr(self.board).diagonal()))==1 and not np.fliplr(self.board).diagonal()[0] == '':
            self.game_end = True

        if self.game_end:
            self.t.configure(state='normal')
            self.t.insert(INSERT, "      {} won the Game!".format(self.player))
            self.t.configure(state='disabled')
            self.t.pack()
            self.b.pack()

        elif not '' in set(self.board.flatten()):
            self.t.configure(state='normal')
            self.t.insert(INSERT, "        The game is Tied")
            self.t.configure(state='disabled')
            self.t.pack()
            self.b.pack()

    def reset(self):
        self.board = np.zeros((self.board_size, self.board_size), dtype=str)
        self.c.delete("all")
        self.drawBoard()
        self.t.configure(state='normal')
        self.t.delete(1.0,END)
        self.t.configure(state='disabled')
        self.b.pack_forget()
        self.game_end = False

    def getorigin(self, eventorigin):
        if not self.game_end:
            buffer = 5
            x = eventorigin.x
            y = eventorigin.y
            if (x >= buffer and y >= buffer) and (x <= self.canvas_width + buffer and y <= self.canvas_height + buffer):
                self.play(x,y)

    def play(self, x, y):
        x, y = self.getBox(x, y)
        if x < self.board_size and y < self.board_size and self.board[x][y] == '':
            self.player = self.players[self.player_index]
            self.move(x, y, self.player)
            self.drawMove(x, y, self.player)
            self.checkEnd()
            if self.player_index < len(self.players) - 1:
                self.player_index += 1
            else:
                self.player_index = 0
    def getBox(self, x, y):
        return floor(y / (self.canvas_width / self.board_size)), floor(x / (self.canvas_height / self.board_size))

    def drawBoard(self):
        for i in range(self.board_size-1):
            self.c.create_line(self.canvas_width * (i + 1) / self.board_size, 0,
                               self.canvas_width * (i + 1) / self.board_size, self.canvas_height, fill="white",
                               width=self.line_thickness)
            self.c.create_line(0, self.canvas_height * (i + 1) / self.board_size, self.canvas_width,
                               self.canvas_height * (i + 1) / self.board_size,
                               fill="white", width=self.line_thickness)

    def drawMove(self, x, y, player):
        print('Drawing move')
        self.c.create_text(y*self.canvas_width/self.board_size+self.canvas_width/(2*self.board_size),
                           x*self.canvas_height/self.board_size+self.canvas_width/(2*self.board_size),
                           fill="black", font="Helvetica {} bold".format(self.font_size), text=player)

if __name__ == "__main__":
    ttt = TicTacToe(players = ['X','O'], board_size=3, font_size = 100)

