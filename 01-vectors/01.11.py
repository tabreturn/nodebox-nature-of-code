# Example 1.11: Array of movers accelerating towards the mouse

from math import sqrt

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
        #print(self.x*self.x + self.y*self.y)
        
class Mover:
    def __init__(self):
        self.location = PVector(random(WIDTH), random(HEIGHT))
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


speed(30)
size(200, 200)
background(1)

def setup():
    global movers
    movers = [None]*20
    for i in range(len(movers)):
        movers[i] = Mover()

def draw():
    global movers
    for i in range(len(movers)):
        movers[i].update()
        movers[i].checkEdges()
        movers[i].display()


