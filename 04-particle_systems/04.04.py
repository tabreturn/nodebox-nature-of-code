from PVector import *

class Particle:
    def __init__(self, l):
        self.location = l.get()
        self.velocity = PVector(random(-1.,1.), random(-2.,0))
        self.acceleration = PVector(0, 0.05)
        self.lifespan = 1.0
    
    def run(self):
        self.update()
        self.display()
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= 0.0075
    
    def display(self):
        stroke(0, self.lifespan)
        fill(0.6, self.lifespan)
        oval(self.location.x, self.location.y, 8, 8)
    
    def isDead(self):
        if(self.lifespan < 0.0):
            return True
        else:
            return False

class ParticleSystem:
    def __init__(self, location):
        self.particles = []
        self.origin = location 
    
    def addParticle(self):
        self.particles.append(Particle(self.origin))
    
    def run(self):
        for i in range(len(self.particles)-1):
            self.particles[i].run()
            if(self.particles[i].isDead()):
                self.particles.pop(i)


size(600, 200)
speed(60)
background(1)

def setup():
    global systems
    systems = []
    
def draw():
    global systems
    if mousedown: # no mouseup function; may be slow as a result
        systems.append(ParticleSystem(PVector(MOUSEX, MOUSEY)))
    for i in range(len(systems)):
        systems[i].run()
        systems[i].addParticle()


