x=0
y=0
jump=False
move=1
def setup():
    size(1000,800)
def draw():
    circle(x,y,100)
def keyPressed():
    global x,y
    if key == 'd':
        x+=5
    if key == 'a':
        x-=5
    if key == 'w':
        y-=5
    if key == 's':
        y+=5
