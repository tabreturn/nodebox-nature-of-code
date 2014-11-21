# Example 3.8: Static wave drawn as a continuous line

from math import sin

def map(value, in_from, in_to, out_from, out_to):
    out_range = out_to-out_from
    in_range = in_to-in_from
    in_val = value-in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val

angle = 0
angleVel = 0.2
amplitude = 100

size(400, 200)
background(1)

stroke(0)
strokewidth(2)
nofill()
autoclosepath(False)

beginpath(0, 0)
for x in range(0, WIDTH, 5):
    y = map(sin(angle), -0.5, 0.5, 0, HEIGHT)
    lineto(x, y)
    angle += angleVel
endpath()


