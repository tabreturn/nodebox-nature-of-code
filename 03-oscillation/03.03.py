from math import sqrt
from math import atan2

class PVector:
    def __init__(self, x_=0, y_=0):
        self.x = x_
        self.y = y_
        
    def add(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y
    
    def sub(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
    
    @staticmethod
    def subStatic(v1, v2):
        v3 = PVector(v1.x-v2.x, v1.y-v2.y)
        return v3
    
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
    
    def limit(self, max):
        if(self.mag() > max):
            self.normalize()
            self.mult(max)
    
    def random2D(self):
        self.x = random(-1., 1.)
        self.y = random(-1., 1.)
        self.normalize()
    
class Mover:
    def __init__(self):
        self.location = PVector(WIDTH/2, HEIGHT/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector()
        self.topspeed = 4
        
    def update(self):
        self.mouse = PVector(MOUSEX, MOUSEY)
        self.dir = PVector.subStatic(self.mouse, self.location)
        
        self.dir.normalize()
        self.dir.mult(0.5)
        self.acceleration = self.dir
        
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
        
    def display(self):
        angle = atan2(self.velocity.y, self.velocity.x) * -1
        
        stroke(0)
        fill(0.6)
        
        push()
        transform(CORNER)
        translate(self.location.x, self.location.y)
        rotate(radians = angle)
        rect(-15, -5, 30, 10)
        pop()
    
    def checkEdges(self):
        if(self.location.x > WIDTH):
            self.location.x = 0
        elif(self.location.x < 0):
            self.location.x = WIDTH
        
        if(self.location.y > HEIGHT):
            self.location.y = 0
        elif(self.location.y < 0):
            self.location.y = HEIGHT


speed(30)
size(600, 600)
background(1)

def setup():
    global mover
    mover = Mover()

def draw():
    global mover
    mover.update()
    mover.checkEdges()
    mover.display()


