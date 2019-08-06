import numpy as np
from tkinter import *

class TicTacToe:

    def __init__(self, player1, player2):
        self.board = np.zeros((3,3), dtype=str)
        self.printBoard()
        self.player1 = player1
        self.player2 = player2

    def move(self, x, y, player):
        self.board[x-1][y-1] = player
        self.printBoard()

    def printBoard(self):
        print(re.sub('[\[\]]', '', np.array_str(self.board)))

    def play(self):
        while True:
            move = input("Player1: ").split(",")
            ttt.move(int(move[0]), int(move[1]), 'X')
            if self.checkEnd():
                print()
                print("Player1 won")
                break
            move = input("Player2: ").split(",")
            ttt.move(int(move[0]), int(move[1]), 'O')
            if self.checkEnd():
                print()
                print("Player2 won")
                break

    def checkEnd(self):
        for i in range(0,3):
            if len(set(self.board[i]))==1 and not self.board[i][0] == '':
                end = True
                break
            elif len(set(self.board[:, i]))==1 and not self.board[:, i][0] == '':
                end =  True
                break
            else:
                end =  False

        if len(set(np.diagonal(self.board)))==1 and not np.diagonal(self.board)[0] == '':
            end = True
        if len(set(np.fliplr(self.board).diagonal()))==1 and not np.fliplr(self.board).diagonal()[0] == '':
            end = True
        return end


if __name__ == "__main__":
    ttt = TicTacToe(1,0)
    ttt.play()
    
