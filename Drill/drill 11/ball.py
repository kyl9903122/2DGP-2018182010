import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
        self.collide_with_tile = False
        self.move_speed, self.dir = 0, 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x+10,self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        self.Move()

    #fill here for def stop
    def stop(self):
        self.fall_speed = 0

    def get_tile_inf(self,move_speed, dir):
        self.move_speed = move_speed
        self.dir = dir

    def change_collide_with_tile(self):
        self.colide_with_tile = True

    def Move(self):
        if self.collide_with_tile:
            self.x += self.dir*self.move_speed*game_framework.frame_time
            if self.x<20 and self.dir == -1:
                self.dir = 1
            elif self.x>1000-20 and self.dir == 1:
                self.dir = -1

# fill here
# class BigBall
class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x,self.y = random.randint(0,900-1),500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,BigBall.MAX_FALL_SPEED)
        self.collide_with_tile = False
        self.move_speed, self.dir = 0, 0

    def get_bb(self):
        return self.x- 20,self.y - 20, self.x +20, self.y+20

    def stop(self):
        self.fall_speed = 0

    def get_tile_inf(self, move_speed, dir):
        self.move_speed = move_speed
        self.dir = dir

    def change_collide_with_tile(self):
        self.collide_with_tile = True

    def Move(self):
        if self.collide_with_tile:
            self.x += self.dir * self.move_speed * game_framework.frame_time
            if self.x < 20 and self.dir == -1:
                self.dir = 1
            elif self.x > 1000 - 20 and self.dir == 1:
                self.dir = -1