from graphics import *
import time
win = GraphWin("color test",1000,1000)
def checkRectangle(point,rectangle):
    return () and ()
class colorRectangle(object):
    rectangles = []
    def __init__(self,p1,p2,color,win):
        self.p1 = p1
        self.p2 = p2
        self.pointUL = self.p1
        self.pointLL = (self.p1[0],self.p2[1])
        self.pointUR = (self.p2[0],self.p1[1])
        self.pointLR = self.p2
        self.points = [self.pointUL,self.pointLL,self.pointUR,self.pointLR]
        self.color = color
        self.win = win
        self.rectangle = Rectangle(Point(self.p1[0],self.p1[1]),Point(self.p2[0],self.p2[1]))
        self.rectangle.draw(self.win)
        self.rectangle.setFill(color_rgb(self.color[0],self.color[1],self.color[2]))
        colorRectangle.rectangles.append(self)
    def __str__(self):
        string = "UL: " + str(self.pointUL)
        string += "\n" + "LL: " + str(self.pointLL)
        string += "\n" + "UR: " + str(self.pointUR)
        string += "\n" + "LR: " + str(self.pointLR) + "\n"
        return string
    def move(self):
        key = self.win.checkKey()
        if key != None:
            if key == "Up":
                self.rectangle.move(0,-1)
                self.pointUL = (self.pointUL[0],self.pointUL[1] - 1)
                self.pointLL = (self.pointLL[0],self.pointLL[1] - 1)
                self.pointUR = (self.pointUR[0],self.pointUR[1] - 1)
                self.pointLR = (self.pointLR[0],self.pointLR[1] - 1)
                self.points = [self.pointUL,self.pointLL,self.pointUR,self.pointLR] 
            elif key == "Down":
                self.rectangle.move(0,1)
                self.pointUL = (self.pointUL[0],self.pointUL[1] + 1)
                self.pointLL = (self.pointLL[0],self.pointLL[1] + 1)
                self.pointUR = (self.pointUR[0],self.pointUR[1] + 1)
                self.pointLR = (self.pointLR[0],self.pointLR[1] + 1)
                self.points = [self.pointUL,self.pointLL,self.pointUR,self.pointLR]
            elif key == "Right":
                self.rectangle.move(1,0)
                self.pointUL = (self.pointUL[0] + 1,self.pointUL[1])
                self.pointLL = (self.pointLL[0] + 1,self.pointLL[1])
                self.pointUR = (self.pointUR[0] + 1,self.pointUR[1])
                self.pointLR = (self.pointLR[0] + 1,self.pointLR[1])
                self.points = [self.pointUL,self.pointLL,self.pointUR,self.pointLR]
            elif key == "Left":
                self.rectangle.move(-1,0)
                self.pointUL = (self.pointUL[0] - 1,self.pointUL[1])
                self.pointLL = (self.pointLL[0] - 1,self.pointLL[1])
                self.pointUR = (self.pointUR[0] - 1,self.pointUR[1])
                self.pointLR = (self.pointLR[0] - 1,self.pointLR[1])
                self.points = [self.pointUL,self.pointLL,self.pointUR,self.pointLR]
rectangle = colorRectangle((0,0),(250,250),(0,0,0),win)
rectangle1 = colorRectangle((250,0),(500,250),(255,255,255),win)
while True:
    points = rectangle.points
    rectangle.move()
    if rectangle.points != points:
        print(rectangle)
    time.sleep(.01)
    


