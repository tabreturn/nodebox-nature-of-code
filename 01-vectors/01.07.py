from math import sqrt

class PVector:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_
        
    def add(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y

    def sub(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
    
    def mult(self, n):
        self.x = self.x * n
        self.y = self.y * n
        
    def div(self, n):
        self.x = self.x / n
        self.y = self.y / n
        
    def mag(self):
        return sqrt(self.x*self.x + self.y*self.y)
        
    def normalize(self):
        m = self.mag()
        if(m != 0):
            self.div(m)

class Mover:
    def __init__(self):
        self.location = PVector(0, 0)
        self.velocity = PVector(random(-2.,2.), random(-2.,2.))
    
    def update(self):
        self.location.add(self.velocity)
    
    def display(self):
        stroke(0)
        fill(0.6, 0.6)
        oval(self.location.x, self.location.y, 16, 16)
    
    def checkEdges(self):
        if(self.location.x > WIDTH):
            self.location.x = 0
        elif(self.location.x < 0):
            self.location.x = WIDTH
        
        if(self.location.y > HEIGHT):
            self.location.y = 0
        elif(self.location.y < 0):
            self.location.y = HEIGHT


speed(60)
size(200, 200)
background(1)

def setup():
    global mover
    mover = Mover()

def draw():
    global mover
    mover.update()
    mover.checkEdges()
    mover.display()


