import pgzrun
TITLE="Gallaga"
WIDTH=1200
HEIGHT=600
speed=5
gallaga=Actor("player")
gallaga.pos=(WIDTH/2,HEIGHT-50)
bugs=[]
for col in range(8):
    for row in range(4):
        bugs.append(Actor("bug.png"))
        bugs[-1].x=100+(50*col)
        bugs[-1].y=80+(50*row)
bullets=[]
def draw():
    screen.fill("black")
    gallaga.draw()
    for bullet in bullets:
        bullet.draw()
    for b in bugs:
        b.draw()

def update():
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

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=gallaga.x
        bullets[-1].y=gallaga.y

pgzrun.go()
