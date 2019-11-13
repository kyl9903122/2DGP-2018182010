import game_framework
from pico2d import *

import game_world

# bird speed
PIXEL_PER_METER = ( 1 / 5.0)
RUN_SPEED_KMPH = 15.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# bird frame
TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class BIRD:
    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.frame_line = 0

    def update(self):
        self.frame = (self.frame + ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time) % 14
        if dir == -1:
            self.velocity += RUN_SPEED_PPS
        else:
            self.velocity -= RUN_SPEED_PPS
        #self.dir = clamp(-1, self.velocity, 1)
        self.x += self.velocity * game_framework.frame_time
        print("velocity:", velocity, "self.x:", self.x, "dir: ", self.dir)
        if self.x < 91 and self.dir == 1:
            print("self.x: ", self.x , "self.dir: ", self.dir)
            self.dir = -1
            self.velocity = 0
        elif self.x>1600-91 and self.dir == -1:
            print("self.x: ", self.x, "self.dir: ", self.dir)
            self.dir = 1
            self.velocity = 0


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame % 5) * 182, int(self.frame/5) * 162, 182, 162, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame % 5) * 182, int(self.frame/5) * 162, 182, 162, 0, 'h', self.x, self.y,182,162)

    def handle_event(self, event):
        pass
