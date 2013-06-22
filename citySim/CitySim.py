from graphics import *
from People import * 

def main():
        win = GraphWin(800, 800)
        for i in range(100):
            person = People()
            cir = Circle(person.width)
            win.draw(cir)












main()
