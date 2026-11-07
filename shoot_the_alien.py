import pgzrun,random

WIDTH,HEIGHT=800,600
message="catch the alien 😊"
score=0
alien=Actor("alien.webp")
alien.pos=200,200

alien2=Actor("alien_2-removebg-preview.png")
alien2.pos=150,200

def draw():
    screen.blit("spaceshipbackground.jpg",(0,0))
    alien.draw()
    alien2.draw()
    screen.draw.text(message,(20,20))
def on_mouse_down(pos):
    global message,score
    print(pos)
    if alien.collidepoint(pos):
        message="yes you caught the right alien😊 "
        score=score+10
        x=random.randint(50,750)
        y=random.randint(50,550)
        alien.pos=x,y
    if alien2.collidepoint(pos):
        message="oops you caught the wrong one :( ) "
        score=score-5
        x=random.randint(50,750)
        y=random.randint(50,550)
        alien2.pos=x,y
pgzrun.go()
