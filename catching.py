import pgzrun,random,pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="catching game"
tom=Actor("tom.webp")
tom.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
jerry=Actor("jerry.jpg")
jerry.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)


def draw():
    screen.blit("bg.webp",(0,0))
    tom.draw()
    jerry.draw()


pgzrun.go()
