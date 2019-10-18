from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x , self.y = random.randint(100, 300), 90
        self.frame = random.randint(0,8)
        self.image = load_image('run_animation.png')
        self.speed = random.randint(4, 8)

    def update(self):
        #update: 상태를 바꿔준다(Game Logic)
        self.frame = (self.frame+1) % 8
        self.x += self.speed

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.size = random.randint(0, 1)
        if(self.size == 0):
            self.x, self.y = random.randint(100, 600), 490
        else:
            self.x, self.y = random.randint(100, 600), 480
        self.speed = random.randint(7, 15)
        if(self.size == 0):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        self.y -=self.speed
        if(self.size == 0):
            if(self.y<=60):
                self.y = 60
        else:
            if(self.y<=70):
                self.y = 70

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
boy = Boy()
team = [Boy() for i in range(11)]
grass = Grass()
ball = Ball()
balls = [Ball() for i in range(20)]

running =True

# game main loop code
while running:
    handle_events(700, 500)

    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)

# finalization code