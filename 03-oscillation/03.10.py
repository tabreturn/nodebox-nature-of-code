# Example 3.10: Swinging pendulum

from math import pi
from math import sin
from math import cos

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

class Pendulum:
    def __init__(self, origin_, r_):
        self.location = PVector()
        self.r = 0.
        self.angle = 0.
        self.aVelocity = 0.
        self.aAcceleration = 0.
        self.damping = 0.
        
        self.origin = origin_.get()
        self.location = PVector()
        self.r = r_
        self.angle = pi/4
        
        self.aVelocity = 0.
        self.aAcceleration = 0.
        self.damping = 0.995
    
    def go(self):
        self.update()
        self.display()
    
    def update(self):
        gravity = 0.4
        self.aAcceleration = (-1 * gravity / self.r) * sin(self.angle)
        self.aVelocity += self.aAcceleration
        self.angle += self.aVelocity
        self.aVelocity *= self.damping
        
    def display(self):
        self.location.x = self.r * sin(self.angle)
        self.location.y = self.r * cos(self.angle)
        
        self.location.add(self.origin)
        stroke(0)
        line(self.origin.x, self.origin.y, self.location.x, self.location.y)
        fill(0.6)
        oval(self.location.x-8, self.location.y-8, 16, 16)


speed(60)
size(400, 400)
background(1) 

def setup():
    global p
    p = Pendulum(PVector(200, 10), 125)

def draw():
    global p
    p.go()


