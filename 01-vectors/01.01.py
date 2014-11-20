class Walker:
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
    
    def step(self):
        r = random(1.0)
        if(r < 0.4):
            self.x += 1
        elif(r < 0.6):
            self.x -= 1
        elif(r < 0.8):
            self.y += 1
        else:
            self.y -= 1
    
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


