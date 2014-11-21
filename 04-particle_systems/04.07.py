# Example 4.7: ParticleSystem with repeller

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
        for i in range(len(self.particles)):
            self.particles[i].applyForce(f)
    
    def applyRepeller(self, r):
        for i in range(len(self.particles)):
            force = r.repel(self.particles[i])
            self.particles[i].applyForce(force)
    
    def run(self):
        for i in range(len(self.particles)-1):
            self.particles[i].run()
            if(self.particles[i].isDead()):
                self.particles.pop(i)

class Repeller:
    def __init__(self, x, y):
        self.r = 10.
        self.location = PVector(x, y)
        self.strength = 100
    
    def display(self):
        stroke(0)
        fill(1)
        oval(self.location.x, self.location.y, self.r*2, self.r*2)
        
    def repel(self, p):
        dir = PVector.subStatic(self.location, p.location)
        d = dir.mag()
        dir.normalize()
        d = self.constrain(d, 5, 100)
        force = -1 * self.strength / (d * d)
        dir.mult(force)
        return dir
    
    def constrain(self, amt, low, high):
        if amt < low: return low
        elif amt > high: return high
        else: return amt


speed(60)
size(640, 360)
background(1)

def setup():
    global ps, repeller
    ps = ParticleSystem(PVector(WIDTH/2, HEIGHT/2))
    repeller = Repeller(WIDTH/2-10, HEIGHT/2+30)
    
def draw():
    global ps, repeller

    ps.addParticle()
    gravity = PVector(0, 0.1)
    ps.applyForce(gravity)
    ps.applyRepeller(repeller)
    
    ps.run()
    repeller.display()


