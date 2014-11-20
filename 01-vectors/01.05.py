from math import *

class PVector:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

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


speed(60)
size(200, 200)
background(1)

def setup():
    global mouse, center

def draw():
    global mouse, center
    mouse = PVector(MOUSEX, MOUSEY)
    center = PVector(WIDTH/2, HEIGHT/2)
    mouse.sub(center)
    
    m = mouse.mag()
    fill(0)
    rect(0, 0, m, 10)
        
    translate(WIDTH/2, HEIGHT/2)
    stroke(0)
    line(0, 0, mouse.x, mouse.y)


