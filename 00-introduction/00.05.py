# Example I.5: Perlin noise walker

from Simplex import *

def map(value, in_from, in_to, out_from, out_to):
    out_range = out_to-out_from
    in_range = in_to-in_from
    in_val = value-in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val


class Walker:
    def __init__(self):
        self.tx = 0
        self.ty = 10000
    
    def step(self):
        xnoise = octave_noise_2d(4, 0.5, 10, self.tx, 1)
        ynoise = octave_noise_2d(4, 0.5, 10, 1, self.ty)
        self.x = map(xnoise, -0.5, 0.5, 0, WIDTH)
        self.y = map(ynoise, -0.5, 0.5, 0, HEIGHT)
        self.tx += 0.0002
        self.ty += 0.0002
    
    def display(self):
        stroke(0)
        fill(0.6)
        oval(self.x, self.y, 50, 50)


speed(60)
size(640, 360)

def setup():
    global w
    w = Walker()

def draw():
    w.step()
    w.display()


