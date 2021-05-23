lst_walls=[]
lst_spike = []
lst_gun = []
lst_ladder = []
class player:
    def __init__(self,x,y,ys,speed,R,L):
        self.x = x
        self.y = y
        self.ys = ys
        self.speed = speed
        self.R = R
        self.L = L
    def draw_(self):
        #rect(self.x,self.y,30,40)
        #image(playerModel[0],self.x,self.y+6,40,40)
        if key == 'a':
            self.L = 1
            self.R = 0
        if self.L == 1:
            image(playerModel[0],self.x,self.y+6,40,40)
        if key =='d':
            self.R = 1
            self.L = 0
        if self.R == 1:
            image(playerModel[1],self.x,self.y+6,40,40)
    def jump(self):
        self.y -= 6
    def move(self,x,y):
        for i in lst_walls:
            if i.cret(self.x + x, self.y+ y) == 1:
                return
            if i.cret(self.x + 30 + x, self.y+ y) == 1:
                return
            if i.cret(self.x + x, self.y+ 40+ y) == 1:
                return
            if i.cret(self.x + 30+ x, self.y+40+ y) == 1:
                return  
            
        for i in lst_spike:
            if i.cret1(self.x + x, self.y+ y) == 1:
                pl.x = 200
                pl.y = 0
            if i.cret1(self.x + 15 + x, self.y+ y) == 1:
                pl.x = 200
                pl.y = 0
            if i.cret1(self.x + x, self.y+ 20+ y) == 1:
                pl.x = 200
                pl.y = 0
            if i.cret1(self.x + 15+ x, self.y+20+ y) == 1:
                pl.x = 200
                pl.y = 0   
        for i in lst_gun:
            if i.cret2(self.x + x, self.y+ y) == 1:
                pl.x = 200
                pl.y = 0
            if i.cret2(self.x + 15 + x, self.y+ y) == 1:
                pl.x = 200
                pl.y = 0
            if i.cret2(self.x + x, self.y+ 20+ y) == 1:
                pl.x = 200
                pl.y = 0
            if i.cret2(self.x + 15+ x, self.y+20+ y) == 1:
                pl.x = 200
                pl.y = 0 
        self.x +=x
        self.y +=y
    
    
    
class platform:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw_(self):
        
        #rect(self.x,self.y,self.w,self.h)
        image(platformModel[0],self.x,self.y,self.w,self.h)
    def cret(self,x,y):
        point(x,y)
        if x > self.x and x < self.x  + self.w and y > self.y and y < self.y + self.h:
            return 1
        else:
            return 0
    
        if pl.x + 15 > self.x and pl.x + 15 < self.x + self.w and pl.y + 45 > self.y and pl.y + 45 < self.y + self.h:
            jumpMODE = 1

class forg:
    def __init__(self,x,y,left,right,speed):
        self.x = x
        self.y = y
        self.left = left
        self.right = right 
        self.speed = speed   
    def draw_(self):
        rect(self.x,self.y,30,30)
        if self.left == 1:
            image(sickerModelL[0],self.x,self.y-6,40,40)
        if self.right == 1:
            image(sickerModelR[0],self.x,self.y-6,40,40)
    def sleg(self):

        if self.left == 1:
            self.x -= self.speed
        if self.right == 1:
            self.x += self.speed
        
        if self.x <= 0:
            self.right = 1
            self.left = 0
        if self.x >= 970:
            self.right = 0
            self.left = 1
            
        if self.y < 370:
            self.y += 4
        if pl.y+ 40 >= 560:
            if self.x < pl.x:
                self.right = 1
                self.left = 0
                self.x += 4
            if self.x > pl.x:
                self.right = 0
                self.left = 1
                self.x -= 4
        else:        
            fors.speed = 1
class final:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw_(self):
        rect(self.x,self.y,20,50)
class spike:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw_(self):
        fill(0)
        rect(self.x,self.y,self.w,self.h)
        fill(255)
    def cret1(self,x,y):
        point(x,y)
        if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
            return 1
        else:
            return 0
        if pl.x + 15 > self.x and pl.x + 15 < self.x + 30 and pl.y + 20 > self.y and pl.y + 20 < self.y + 30:
            pl.x = 200
            pl.y = 0

class gun:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw_(self):
        circle(self.x,self.y,20)
        self.x -= 5
        if self.x < 0:
            self.x == 400  
    def cret2(self,x,y):
        point(x,y)
        if x > self.x and x < self.x + 10 and y > self.y and y < self.y + 0:
            return 1
        else:
            return 0
    def move(self):
        self.x -= 5
        if self.x < 0:
            self.x == 400 
        
class ladder:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw_(self):
        push()
        fill("#FF9900")
        rect(self.x,self.y,self.w,self.h)
        pop()
        if pl.x + 15 > self.x and pl.y + 20 > self.y and pl.x + 15 < self.x + self.w and pl.y + 20 < self.y + self.h:
            pl.y -= 7
  
fors = forg(200,570,1,0,1)
pl = player(200,40,200,5,0,1)
jumpMODE = 0
group = [ ["30","370"],["50","250"] ]
fruitMode = 1
final = final(980,550)

def setup():
    lst_walls.append(platform(0,-10,1000,10))
    
    lst_walls.append(platform(0,310,100,10))
    lst_walls.append(platform(0,310,100,10))
    lst_walls.append(platform(300,310,100,10))
    lst_walls.append(platform(150,250,100,10))
    lst_walls.append(platform(0,210,100,10))
    lst_walls.append(platform(300,210,100,10))
    lst_walls.append(platform(0,410,100,10))
    lst_walls.append(platform(300,410,100,10))
    lst_walls.append(platform(0,510,100,10))
    lst_walls.append(platform(300,510,100,10))
    lst_walls.append(platform(150,510,100,10))
    lst_walls.append(platform(150,340,100,10))


    lst_walls.append(platform(430,510,100,10))
    lst_walls.append(platform(500,450,100,10))
    lst_walls.append(platform(400,390,100,10))
    lst_walls.append(platform(500,330,100,10))
    lst_walls.append(platform(400,270,100,10))
    lst_walls.append(platform(500,205,100,10))
    lst_walls.append(platform(400,140,100,10))
    lst_walls.append(platform(500,70,100,10))
    
    lst_walls.append(platform(150,160,100,10))
    lst_walls.append(platform(0,100,100,10))
    lst_walls.append(platform(300,100,100,10))
    lst_walls.append(platform(150,80,100,10))
    lst_walls.append(platform(600,510,100,10))
    
    lst_walls.append(platform(650,150,50,10))
    lst_walls.append(platform(750,100,100,10))
    
    lst_spike.append(spike(300,180,30,30))
    lst_spike.append(spike(70,180,30,30))
    lst_spike.append(spike(750,100,10,420))
    lst_spike.append(spike(400,0,10,460))
    lst_spike.append(spike(600,70,10,450))
    lst_spike.append(spike(650,0,10,460))
    
    lst_gun.append(gun(1000,300))
    
    lst_ladder.append(ladder(700,100,50,420))

    size(1000,600)
def draw():
    global pl,jumpMODE,platf,fors,group,fruitMode,sickerModelL,sickerModelR,playerModel,platformModel,gun
    background(255)
    print(jumpMODE)
    sickerModelL = [loadImage("sickerL.png")]
    sickerModelR = [loadImage("sickerR.png")]
    playerModel = [loadImage("playerL.png"),loadImage("playerR.png")]
    platformModel = [loadImage("platform.png")]
    fors.draw_()
    fors.sleg()
    pl.draw_()
    final.draw_()
    for i in lst_ladder:
        i.draw_()
    for i in lst_walls:
        i.draw_()
    for i in lst_spike:
        i.draw_()
    for i in lst_gun:
        i.draw_()

        
    if pl.x + 15 > final.x and pl.x + 15 < final.x + 20 and pl.y + 20 > final.y and pl.y + 20 < final.y + 50:
        pl.x = 200
        pl.y = 0
        while len(lst_walls)>0:
            del lst_walls[0]
        while len(lst_spike)>0:
            del lst_spike[0]
        while len(lst_ladder)>0:
            del lst_ladder[0]
        lst_walls.append(platform(0,310,100,10))
        lst_walls.append(platform(0,100,100,10))
        lst_walls.append(platform(150,140,100,10))
        lst_walls.append(platform(300,180,100,10))
        lst_walls.append(platform(200,220,100,10))
        lst_walls.append(platform(100,270,270,10))
        lst_walls.append(platform(370,210,10,50))
        
        lst_spike.append(spike(350,150,30,30))
        lst_spike.append(spike(100,350,300,30))
        
    

    if keyPressed:
        if pl.x < 970:
            if key == 'd':
                #pl.x += 3
                pl.move(3,0)

        if pl.x > 0:
            if key == 'a':
                #pl.x -= 3
                pl.move(-3,0)


    if pl.y < 560 and pl.y+40 > 0:
        #pl.y += pl.speed
        pl.move(0,2)

    if jumpMODE == 1:
        for i in lst_walls:
            if i.cret(pl.x, pl.y - 6) == 1:
                pl.ys = pl.y
            elif i.cret(pl.x + 30, pl.y - 6) == 1:
                pl.ys = pl.y
        if pl.y > pl.ys:
            pl.move(0,-6)
    if pl.y == pl.ys:
        jumpMODE = 0
 
    if pl.x + 15 > fors.x and pl.x + 15 < fors.x + 30 and pl.y + 20 > fors.y and pl.y + 20 < fors.y + 30:
        pl.x = 200
        pl.y = 0

def keyPressed():
    global pl,jumpMODE
    if key == ' ':
        pl.ys = pl.y - 70
        jumpMODE = 1
    
