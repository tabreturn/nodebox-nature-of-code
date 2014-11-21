# Example 1.3: Vector subtraction

class PVector:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_
        
    def sub(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y


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
    
    translate(WIDTH/2, HEIGHT/2)
    
    stroke(0)
    line(0, 0, mouse.x, mouse.y)


