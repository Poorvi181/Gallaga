import pgzrun
TITLE="Gallaga"
WIDTH=1200
HEIGHT=600
score=0
direction=1
speed=5
gallaga=Actor("player")
gallaga.pos=(WIDTH/2,HEIGHT-50)
gallaga.dead=False
gallaga.countdown=90
bugs=[]
for col in range(8):
    for row in range(4):
        bugs.append(Actor("bug.png"))
        bugs[-1].x=100+(50*col)
        bugs[-1].y=80+(50*row)
bullets=[]
def draw():
    screen.fill("black")
    if gallaga.dead==False:
        gallaga.draw()
    for bullet in bullets:
        bullet.draw()
    for b in bugs:
        b.draw()

def update():
    global direction,score
    movedown=False
    if keyboard.left:
        gallaga.x-=speed
        if gallaga.x<0:
            gallaga.x=0
    if keyboard.right:
        gallaga.x+=speed
        if gallaga.x>WIDTH:
            gallaga.x=WIDTH
    for bullet in bullets:
        if bullet.y<0:
            bullets.remove(bullet)
        else:
            bullet.y-=10
    if len(bugs)>0 and (bugs[0].x<80 or bugs[-1].x>WIDTH-80):
        direction=direction*(-1)
        movedown=True
    
        
    for bug in bugs:
        bug.x+=4*direction
        for bullet in bullets:
            if bullet.colliderect(bug):
                bugs.remove(bug)
                bullets.remove(bullet)
                score+=1
                sounds.sound.play()
        if movedown:
            bug.y+=20
        if bug.colliderect(gallaga):
            gallaga.dead=True

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=gallaga.x
        bullets[-1].y=gallaga.y

pgzrun.go()
