from math import radians

speed(60)
size(640, 360)
background(1)

def setup():
    global angle, aVelocity, aAcceleration
    angle = radians(60)
    aVelocity = 0
    aAcceleration = 0.001

def draw():
    global angle, aVelocity, aAcceleration
    
    fill(0.6)
    stroke(0)
    transform(CORNER)
    translate(WIDTH/2, HEIGHT/2)
    rotate(radians=angle)
    line(-50, 0, 50, 0)
    oval(50, -4, 8, 8)
    oval(-58, -4, 8, 8)
    
    aVelocity += aAcceleration
    angle += aVelocity


