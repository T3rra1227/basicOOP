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
        self.ySpeed = -10
        self.xSpeed = 8
    
    def move(self, lives):
        self.yPos += self.ySpeed
        self.xPos += self.xSpeed
        if self.yPos < 0:
            self.ySpeed *= -1
        if self.yPos > 900:
            lives -= 1
            self.ySpeed *= -1
            self.yPos = 700
            self.xPos = 500
        if self.xPos > 1000 or self.xPos < 0:
            self.xSpeed *= -1
            #xPos = 1000
        
        drawEllipse(self.xPos, self.yPos, 20, 20, self.colour)
        
        return lives
        
class Brick():
    def __init__(self,x,y, colour):
    #attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.width = 75
        self.height = 50
        self.active = True
        
    def draw(self):
        if self.active:
            drawRect(self.xPos,self.yPos,self.width, self.height, self.colour)
        
    def detectHit(self,balls):
        for ball in balls:
            if self.xPos <= ball.xPos <= self.xPos + self.width:
                if self.yPos <= ball.yPos <= self.yPos + self.height:
                    ball.ySpeed *= -1
                    return True
        return False
    
    def update(self,balls):
        self.draw()
        if self.active and self.detectHit(balls):
            self.active = False
        
class Bat(Brick): # inherits the Brick class: all the traits brick has, bat now has - appears on exams
    def __init__(self,x,y,colour):
        super().__init__(x,y,colour)
        self.width = 150
        self.height = 25
        
    def update(self,balls): #overriding brick data
        self.draw()
        self.detectHit(balls)
        if keyPressed("right"):
            self.xPos += 10
        if keyPressed("left"):
            self.xPos -= 10
    
        if self.xPos > 1150:
            self.xPos = 0
        if self.xPos < 0:
            self.xPos = 110
        
class MultiBrick(Brick):
    def update(self,balls):
        self.draw()
        if self.active and self.detectHit(balls):
            self.active = False
            balls.append( Ball(self.xPos, self.yPos, "yellow"))

colours = ["red","orange","purple","blue","green"]
balls = [ Ball(500,500,random.choice(colours)) for i in range(1) ]
bricks = []

for x in range(0,1000,77):
    bricks.append(Brick(x,100,"orange"))
    bricks.append(Brick(x,200,"red"))
    bricks.append(Brick(x,300,"blue"))

randomPos = random.randint(0,len(bricks))
removedBrick = bricks.pop(randomPos)
bricks.insert(randomPos,MultiBrick(removedBrick.xPos,removedBrick.yPos,"black"))


bat = Bat(500,850,"lightblue") # Instantiation
lives = 3
livesLabel = makeLabel("Lives:", 24, 10, 10, "white")
showLabel(livesLabel)
gameOverLabel = makeLabel("GAME OVER", 80, 300, 450,"red")

running = True
while running:
    clearShapes()
    changeLabel(livesLabel, "Lives: " + str(lives))
    bat.update(balls)
    for b in balls:
        lives = b.move(lives)
        if lives <= 0:
            showLabel(gameOverLabel)
            running = False
    for brick in bricks:
        brick.update(balls)
    tick(60)
    updateDisplay()

endWait()
