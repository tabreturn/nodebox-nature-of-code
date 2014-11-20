from math import sin

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

class Oscillator:
    def __init__(self):
        self.angle = PVector()
        self.velocity = PVector(random(-0.05, 0.05), random(-0.05, 0.05))
        self.amplitude = PVector(random(WIDTH/2), random(HEIGHT/2))
        self.angle.add(self.velocity)
        
    def oscillate(self):
        self.angle.add(self.velocity)
        
    def display(self):
        x = sin(self.angle.x) * self.amplitude.x
        y = sin(self.angle.y) * self.amplitude.y
        
        push()
        translate(WIDTH/2, HEIGHT/2)
        stroke(0)
        fill(0.6)
        line(0, 0, x, y)
        oval(x-8, y-8, 16, 16)
        pop()


speed(60)
size(400, 400)
background(1) 

def setup():
    global oscillators
    
    oscillators = [None]*10
    for i in range(len(oscillators)):
        oscillators[i] = Oscillator()

def draw():
    global oscillators
    
    for i in range(len(oscillators)):
        oscillators[i].oscillate()
        oscillators[i].display()


