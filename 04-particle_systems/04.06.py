from PVector import *

class Particle:
    def __init__(self, l):
        self.location = l.get()
        self.velocity = PVector(random(-1.,1.), random(-2.,0))
        self.acceleration = PVector(0, 0)
        self.lifespan = 1.0
        
        self.mass = 1
    
    def run(self):
        self.update()
        self.display()
    
    def applyForce(self, force):
        f = force
        f.div(self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
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
        self.origin = location
        self.particles = []
    
    def addParticle(self):
        self.particles.append(Particle(self.origin))
        
    def applyForce(self, f):
        for i in range(len(self.particles)-1):
            self.particles[i].applyForce(f)
    
    def run(self):
        for i in range(len(self.particles)-1):
            self.particles[i].run()
            if(self.particles[i].isDead()):
                self.particles.pop(i)


speed(60)
size(640, 360)
background(1)

def setup():
    global ps
    ps = ParticleSystem(PVector(WIDTH/2, HEIGHT/2))
    
def draw():
    global ps
    gravity = PVector(0, 0.1)
    ps.applyForce(gravity)
    
    ps.addParticle()
    ps.run()


