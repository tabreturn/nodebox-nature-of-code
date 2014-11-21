# Example 3.9: The Wave

from math import sin

def map(value, in_from, in_to, out_from, out_to):
    out_range = out_to-out_from
    in_range = in_to-in_from
    in_val = value-in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val

size(400, 200)
background(1)
speed(60)

def setup():
    global startAngle, angleVel, angle
    startAngle = 0.
    angleVel = 0.1
    angle = 0.

def draw():
    global startAngle, angleVel, angle
    for x in range(0, WIDTH, 24):
        y = map(sin(angle), -0.5, 0.5, 0, HEIGHT)
        stroke(0)
        fill(0, 0.5)
        oval(x, y, 48, 48)
        angle += angleVel


