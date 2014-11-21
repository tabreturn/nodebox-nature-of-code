# Example I.2: Random number distribution

speed(60)
size(640, 240)
background(1)

def setup():
    global randomCounts
    randomCounts = [0]*20

def draw():
    index = random(len(randomCounts))
    randomCounts[index] += 1
    
    stroke(0)
    fill(0.6, 0.6)
    w = WIDTH/len(randomCounts)
    for x in range(len(randomCounts)):
        rect(x*w, HEIGHT-randomCounts[x], w-1, randomCounts[x])

