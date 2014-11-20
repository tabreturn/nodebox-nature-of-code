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

class Spring:
    def __init__(self, x, y, l):
        self.anchor = PVector(x, y)
        self.len = l
        self.k = 0.1
    
    def connect(self, b):
        force = PVector()
        force = PVector.subStatic(b.location, self.anchor)
        d = force.mag()
        stretch = d - self.len
        
        force.normalize()
        force.mult(-1 * self.k * stretch)
        
        b.applyForce(force)
    
    def display(self):
        fill(0.5)
        rect(self.anchor.x-5, self.anchor.y-5, 10, 10)
    
    def displayLine(self, b):
        stroke(0)
        strokewidth(2)
        line(b.location.x, b.location.y, self.anchor.x, self.anchor.y)

class Bob:
    def __init__(self, x, y):
        self.location = PVector(x, y)
        self.velocity = PVector()
        self.acceleration = PVector()
        self.mass = 24
        self.damping = 0.98
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.mult(self.damping)
        self.location.add(self.velocity)        
        self.acceleration.mult(0)
    
    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)
    
    def display(self):
        stroke(0)
        strokewidth(2)
        fill(0.6)
        oval(self.location.x-self.mass, self.location.y-self.mass, 
             self.mass*2, self.mass*2)


  
speed(60)
size(400, 200)
background(1) 

def setup():
    global bob, spring
    spring = Spring(WIDTH/2, 10, 100)
    bob = Bob(WIDTH/2, 100)

def draw():
    global bob, spring
    gravity = PVector(0, 2)
    bob.applyForce(gravity)
    
    spring.connect(bob)
    bob.update()
    
    spring.displayLine(bob)
    bob.display()
    spring.display()


