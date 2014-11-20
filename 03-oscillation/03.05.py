from math import cos
from math import pi

speed(60)
size(640, 360)
background(1)

def setup():
    global frameCount
    frameCount = 0
    
def draw():
    global frameCount
    frameCount += 1
    
    period = 120
    amplitude = 100
    x = amplitude * cos((2*pi) * frameCount/period)
    
    stroke(0)
    fill(0.6)
    translate(WIDTH/2, HEIGHT/2)
    line(0, 0, x, 0)
    oval(x-10, -10, 20, 20)


