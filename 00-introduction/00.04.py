import random

speed(60)
size(640, 360)

#def setup():
    ###

def draw():
    sd = 60.0
    mean = 320.0
    num = random.gauss(mean, sd)
    x = num
    
    nostroke()
    fill(0, 0.1)
    oval(x, 180, 16, 16)

