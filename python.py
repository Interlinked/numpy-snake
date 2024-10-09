import numpy as np
import time
board = []
class myBoard:
    WIDTH = 10
    HEIGHT = 10
    def createBoard():
        global board
        board = np.arange(myBoard.WIDTH*myBoard.HEIGHT).reshape(myBoard.HEIGHT,myBoard.WIDTH)
        return board
class player:
    LENGTH = 1
    xcord = 0
    ycord = 0
    def createPlayer():
        board = myBoard.createBoard()
        board[player.xcord,player.ycord] = s
        return board
        


myBoard.createBoard()
print(player.createPlayer())

