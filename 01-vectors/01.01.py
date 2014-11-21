# Example 1.10: Accelerating towards the mouse

speed(60)
size(640, 360)
background(1)

def setup():
    global x, y, xspeed, yspeed
    x = 100
    y = 100
    xspeed = 1
    yspeed = 3.3

def draw():
    global x, y, xspeed, yspeed
    x = x + xspeed
    y = y + yspeed
    
    if((x > WIDTH) or (x < 0)):
        xspeed = xspeed * -1
    if((y > HEIGHT) or (y < 0)):
        yspeed = yspeed * -1
    
    stroke(0)
    fill(0.6)
    oval(x,y,16,16)


