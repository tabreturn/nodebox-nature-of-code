from PVector import *
from Particle import *
from math import pi

def map(value, in_from, in_to, out_from, out_to):
    out_range = out_to-out_from
    in_range = in_to-in_from
    in_val = value-in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val


class Vehicle:
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(random(-3,3), random(-3,3))
        self.location = PVector(x, y)
        self.r = 3.
        self.maxspeed = 4.
        self.maxforce = 0.15
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
    
    def applyForce(self, force):
        self.acceleration.add(force)
    
    def seek(self, target):
        desired = PVector.subStatic(target, self.location)
        desired.normalize()
        desired.mult(self.maxspeed)
        steer = PVector.subStatic(desired, self.velocity)
        steer.limit(self.maxforce)
        self.applyForce(steer)
    
    def arrive(self, target):
        desired = PVector.subStatic(target, self.location)
        d = desired.mag()
        desired.normalize()
        if(d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.mult(m)
        else:
            desired.mult(self.maxspeed)
        steer = PVector.subStatic(desired, self.velocity)
        steer.limit(self.maxforce)
        self.applyForce(steer)
           
    def boundaries(self, d):
        desired = False
        
        if(self.location.x < d):
            desired = PVector(self.maxspeed, self.velocity.y)
        elif(self.location.x > WIDTH-d):
            desired = PVector(-self.maxspeed, self.velocity.y)
        
        if(self.location.y < d):
            desired = PVector(self.velocity.x, self.maxspeed)
        elif(self.location.y > HEIGHT-d):
            desired = PVector(self.velocity.x, -self.maxspeed)
        
        if(desired):
            desired.normalize()
            desired.mult(self.maxspeed)
            steer = PVector.subStatic(desired, self.velocity)
            steer.limit(self.maxforce)
            self.applyForce(steer)
    
    def display(self):
        theta = self.velocity.heading() + pi/2
        fill(0,6)
        stroke(0)
        push()
        translate(self.location.x, self.location.y)
        rotate(radians = theta*-1)
        beginpath(0, -self.r*2)
        lineto(-self.r, self.r*2)
        lineto(self.r, self.r*2)
        endpath()
        pop()
    
    def run(self):
        self.update()
        self.display()


speed(60)        
size(800, 400)
background(1)

def setup():
    global d, v
    v = Vehicle(WIDTH/2, HEIGHT/2)
    d = 25

def draw():
    global d, v
    stroke(0.6)
    nofill()
    rect(d, d, WIDTH-(d*2), HEIGHT-(d*2))
         
    v.boundaries(d)
    v.run()


