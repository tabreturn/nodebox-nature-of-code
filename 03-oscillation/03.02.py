# Example 3.2: Forces with (arbitrary) angular motion

from math import sqrt

def constrain(amt, low, high):
        if amt < low: return low
        elif amt > high: return high
        else: return amt


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
        self.velocity = PVector()
        self.acceleration = PVector()
        
        self.angle = 0
        self.aVelocity = 0
        self.aAcceleration = 0
        
    def applyForce(self, force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        
        self.aAcceleration = self.acceleration.x / 10.0
        self.aVelocity += self.aAcceleration
        self.aVelocity = constrain(self.aVelocity, -0.1, 0.1)
        self.angle += self.aVelocity
        
        self.acceleration.mult(0)
        
    def display(self):
        stroke(0)
        fill(0.6, 0.6)
        
        rotate(self.angle)
        
        rect(self.location.x, self.location.y, 16*self.mass, 16*self.mass)
    
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
            
    def isInside(self, l):
        if(self.location.x > l.x and self.location.x < l.x+l.w and 
           self.location.y > l.y and self.location.y < l.y+l.h):
            return True
        else:
            return False
    
    def drag(self, l):
        speed = self.velocity.mag()
        dragMagnitude = l.c * speed * speed
        
        drag = self.velocity.get()
        drag.mult(-1)
        drag.normalize()
        
        drag.mult(dragMagnitude)
        self.applyForce(drag)

class Attractor:
    def __init__(self):
        self.mass = 20
        self.location = PVector(WIDTH/2, HEIGHT/2)
        self.G = 0.4
        
    def attract(self, m):
        force = PVector.subStatic(self.location, m.location)
        distance = force.mag()
        distance = self.constrain(distance, 5.0, 25.0)
        
        force.normalize()
        strength = (self.G * self.mass * m.mass) / (distance * distance)
        force.mult(strength)
        return force
    
    def constrain(self, amt, low, high):
        if amt < low: return low
        elif amt > high: return high
        else: return amt
    
    def display(self):
        stroke(0)
        fill(0.6, 0.5)
        oval(self.location.x, self.location.y, self.mass*2, self.mass*2)


speed(60)
size(400, 400)
background(1)

def setup():
    global movers, a
    
    movers = [None]*10
    for i in range(len(movers)):
        movers[i] = Mover(random(0.1, 2), random(WIDTH), random(HEIGHT))
    
    a = Attractor()

def draw():
    global m, a
    
    a.display()
    
    for i in range(len(movers)):
        force = a.attract(movers[i])
        movers[i].applyForce(force)
        movers[i].update()
        movers[i].display()


