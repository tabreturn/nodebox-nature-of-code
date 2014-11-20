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
        return v3;
    
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
    
    def get(self):
        return PVector(self.x, self.y)
        
class Mover:
    def __init__(self, m, x, y):
        self.mass = m
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        
    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
        
    def display(self):
        stroke(0)
        fill(0.6, 0.6)
        oval(self.location.x, self.location.y, 16*self.mass, 16*self.mass)
    
    def checkEdges(self):
        if(self.location.x > WIDTH):
            self.location.x = WIDTH
            self.velocity.x *= -1
        elif(self.location.x < 0):
            self.velocity.x *= -1
            self.location.x = 0
        
        if(self.location.y > HEIGHT-10):
            self.velocity.y *= -1
            self.location.y = HEIGHT-10


speed(60)
size(200, 200)
background(1)

def setup():
    global movers, wind
    wind = PVector(0.001, 0)
    movers = [None]*5
    for i in range(len(movers)):
        movers[i] = Mover(random(0.1, 5), 0, 0)

def draw():
    global movers, wind
    for i in range(len(movers)):
        m = movers[i].mass
        gravity = PVector(0, 0.01*m)
        movers[i].applyForce(wind)
        movers[i].applyForce(gravity)
        movers[i].update()
        movers[i].checkEdges()
        movers[i].display()


