import game_framework
from pico2d import *
from ball import Ball

import game_world

class TILE:
    image = None

    def __init__(self):
        if self.image == None:
            self.image = load_image('brick180x40.png')
        self.x, self.y, self.move_velocity, self.dir = 300, 200, 100, 1

    def get_bb(self):
        # fill here
        return self.x - 90, self.y - 20, self.x+90,self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.move_velocity * game_framework.frame_time * self.dir
        if self.x < 90 and self.dir == -1:
            self.dir = 1
        elif self.x > 900 -90 and self.dir == 1:
            self.dir = -1

    def get_info(self):
        return self.move_velocity,self.dir


