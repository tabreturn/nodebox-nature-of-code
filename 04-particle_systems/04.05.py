from PVector import *
from math import pi

def map(value, in_from, in_to, out_from, out_to):
    out_range = out_to-out_from
    in_range = in_to-in_from
    in_val = value-in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val


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

class Confetti(Particle):
    def display(self):
        theta = map(self.location.x, 0, WIDTH, 0, (pi*2)*2)
        
        fill(0.6)
        stroke(0)
        push()
        rotate(radians=theta)
        rect(self.location.x-4, self.location.y-4, 8, 8)
        pop()

class ParticleSystem:
    def __init__(self, location):
        self.origin = location
        self.particles = []
    
    def addParticle(self):
        r = random(1.)
        if(r < 0.5):
            self.particles.append(Particle(self.origin))
        else:
            self.particles.append(Confetti(self.origin))
    
    def run(self):
        for i in range(len(self.particles)-1):
            self.particles[i].run()
            if(self.particles[i].isDead()):
                self.particles.pop(i)


speed(60)
size(600, 400)
background(1)

def setup():
    global ps
    ps = ParticleSystem(PVector(WIDTH/2, HEIGHT/2))
    
def draw():
    global ps
    ps.addParticle()
    ps.run()


