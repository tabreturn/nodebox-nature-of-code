# Example 1.4: Multiplying a vector

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


speed(60)
size(200, 200)
background(1)

def setup():
    global location, velocity

def draw():
    global location, velocity
    mouse = PVector(MOUSEX, MOUSEY)
    center = PVector(WIDTH/2, HEIGHT/2)
    mouse.sub(center)
    
    mouse.mult(0.5)
    
    translate(WIDTH/2, HEIGHT/2)
    
    stroke(0)
    line(0, 0, mouse.x, mouse.y)


