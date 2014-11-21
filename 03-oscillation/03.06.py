# Example 3.6: Simple Harmonic Motion II

from math import cos

speed(60)
size(640, 360)
background(1)

def setup():
    global angle, aVelocity
    angle = 0
    aVelocity = 0.05
    
def draw():
    global angle, aVelocity
    
    amplitude = 100
    x = amplitude * cos(angle)
    angle += aVelocity
    
    stroke(0)
    fill(0.6)
    translate(WIDTH/2, HEIGHT/2)
    line(0, 0, x, 0)
    oval(x-10, -10, 20, 20)


