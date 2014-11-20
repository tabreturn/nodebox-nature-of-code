from math import cos
from math import sin

speed(60)
size(640, 360)
background(1)

def setup():
    global r, theta
    r = 75
    theta = 0

def draw():
    global r, theta
    x = r * cos(theta)
    y = r * sin(theta)
    
    nostroke()
    fill(0)
    oval(x+WIDTH/2, y+HEIGHT/2, 16, 16)
    
    theta += 0.01


