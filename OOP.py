from pygame_functions import *
import random

screenSize(1000,900)
setBackgroundColour("darkgreen")
setAutoUpdate(False)

class Ball:
    def __init__(self,x,y, colour):
    #attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.ySpeed = 10
        self.xSpeed = 8
    
    def move(self):
        self.yPos += self.ySpeed
        self.xPos += self.xSpeed
        if self.yPos > 900 or self.yPos < 0:
            self.ySpeed *= -1
        if self.xPos > 1000 or self.xPos < 0:
            self.xSpeed *= -1
            #xPos = 1000
        drawEllipse(self.xPos, self.yPos, 20, 20, self.colour)
        
class Brick():
    def __init__(self,x,y, colour):
    #attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.width = 75
        self.height = 50
        
    def draw(self):
        drawRect(self.xPos,self.yPos,self.width, self.height, self.colour)
        

xPos = 500
yPos = 0
ySpeed = 0
xSpeed = random.randint(-10,10)
nBalls = random.randint(1,1000)

colours = ["red","orange","purple","blue","green"]
balls = [ Ball(random.randint(50,850),0,random.choice(colours)) for i in range(1) ]
bricks = []

for x in range(0,1000,77):
    bricks.append(Brick(x,100,"orange"))
    bricks.append(Brick(x,200,"red"))
    bricks.append(Brick(x,300,"blue"))

while True:
    clearShapes()
    for b in balls:
        b.move()
    for brick in bricks:
        brick.draw()
    tick(60)
    updateDisplay()

endWait()