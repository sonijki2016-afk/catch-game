import pgzrun,random,pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="catching game"
tom=Actor("tom.webp")
tom.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
jerry=Actor("jerry.jpg")
jerry.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
spike = Actor("spike")
spike.pos = (600, 300)
score=0
message="catch jerry dodge spike"
game_over=False
def draw():
    screen.blit("bg.jpg",(0,0))
    tom.draw()
    jerry.draw()
    spike.draw()
    screen.draw.text("message "+message,(50,50))
    screen.draw.text("score="+str(score),(50,80))
def update():
    global score,message
    if keyboard.left and tom.x>50:
        tom.x -= 5

    if keyboard.right and tom.x<WIDTH-50:
        tom.x += 5

    if keyboard.up and tom.y>50: 
        tom.y -= 5

    if keyboard.down and tom.y<HEIGHT-50:
        tom.y += 5

    if jerry.colliderect(tom):
        jerry.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        tom.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        spike.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        score=score+10
        message="GOOD JOB" 

    if spike.colliderect(tom):
        jerry.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        tom.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        spike.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        score=score-5
        message="OOPS spike got you" 
def game_ended():
     global game_over,message
     game_over=True
     message="game_over"
clock.schedule(game_ended,30.0)

pgzrun.go()


