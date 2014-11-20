class PVector:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_
    
    def add(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y


speed(60)
size(200, 200)
background(1)

def setup():
    global location, velocity
    location = PVector(100, 100)
    velocity = PVector(1, 3.3)

def draw():
    global location, velocity
    location.add(velocity)
    
    if((location.x > WIDTH) or (location.x < 0)):
        velocity.x = velocity.x * -1
    if((location.y > HEIGHT) or (location.y < 0)):
        velocity.y = velocity.y * -1
        
    nostroke()
    fill(0.6, 0.6)
    oval(location.x, location.y, 16, 16)


