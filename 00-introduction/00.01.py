class Walker:
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
    
    def step(self):
        self.stepx = random(-1.0, 1.0)
        self.stepy = random(-1.0, 1.0)
        self.x += self.stepx
        self.y += self.stepy
    
    def display(self):
        nostroke()
        rect(self.x, self.y, 1, 1)


speed(60)
size(640, 360)

def setup():
    global w 
    w = Walker()

def draw():
    w.step()
    w.display()

