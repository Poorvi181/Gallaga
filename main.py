import pgzrun
TITLE="Gallaga"
WIDTH=1200
HEIGHT=600
speed=5
gallaga=Actor("player")
gallaga.pos=(WIDTH/2,HEIGHT-50)
bug=Actor("bug")
bug.pos=(WIDTH/2,50)
bullets=[]
def draw():
    screen.fill("black")
    gallaga.draw()
    bug.draw()
def update():
    if keyboard.left:
        gallaga.x-=speed
        if gallaga.x<0:
            gallaga.x=0
    if keyboard.right:
        gallaga.x+=speed
        if gallaga.x>WIDTH:
            gallaga.x=WIDTH
def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
pgzrun.go()