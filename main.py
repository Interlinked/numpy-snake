from time import sleep
import sys
import os
import curses

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.noecho() 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class gameScreen:
    def __init__(self,width,height):
        self.WIDTH = width
        self.HEIGHT = height

        self.board = [[0 for i in range(self.WIDTH)] for j in     range(self.HEIGHT)]
    def refresh(self):
        cls()
        for rows in self.board:
            print("\r",rows)
            
        
class player:
    LENGTH = 1
    ycord = 1
    xcord = 1
    direction = "down"
    def createPlayer():
        return
    def move():
        
        if(player.direction == "right"):
            for rows in screen.board:
                screen.board[player.xcord][player.ycord] = 0
                player.ycord = player.ycord + 1
                screen.board[player.xcord][player.ycord]=9
                screen.refresh()
                print(player.direction)
                sleep(1)
        elif (player.direction =="left"):
            for rows in screen.board:
                screen.board[player.xcord][player.ycord] = 0
                player.ycord = player.ycord - 1
                screen.board[player.xcord][player.ycord]=9
                screen.refresh()
                print(player.direction)
                sleep(1)
        elif (player.direction =="down"):
            for rows in screen.board:
                screen.board[player.xcord][player.ycord] = 0
                player.xcord = player.xcord + 1
                screen.board[player.xcord][player.ycord]=9
                screen.refresh()
                print(player.direction)
                sleep(1)
                
        elif (player.direction =="up"):
            for rows in screen.board:
                screen.board[player.xcord][player.ycord] = 0
                player.xcord = player.xcord - 1
                screen.board[player.xcord][player.ycord]=9
                screen.refresh()
                print(player.direction)
                sleep(1)

screen = gameScreen(10,10)



    
print(player.createPlayer())

while True:
    stdscr.nodelay(1)
    char = stdscr.getch()
    print(char)
    if char == curses.KEY_RIGHT: player.direction = "right"
    elif char == curses.KEY_LEFT: player.direction = "left"
    elif char == curses.KEY_UP: player.direction = "up"
    elif char == curses.KEY_DOWN: player.direction = "down"

    player.move()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
