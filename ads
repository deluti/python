x=0
jump=False
move=1
def setup():
    size(400,400)
def draw():
    background("#FFFFFF")
    circle(x,350,100)
    
    if jump == True:
        if move == 1:
            y+=move
            if y < h1:
                move = h
    else:
        y+=move
        if y > 
def keyPressed():
    global x
    if key == 'd':
        x+=5
    if key == 'a':
        x-=5
