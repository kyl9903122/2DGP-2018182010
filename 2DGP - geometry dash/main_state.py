import random
import json
import os
import title_state
import maptool_state

from pico2d import *

import game_framework
import title_state
import character_class
import background_class
import tile_class
import obstacle_class



name = "MainState"


font = None
character = None
background = None
tiles = None
obstacles_triangle = None
isJump = False
speed = 0
degree = 0

def enter():
    global character, background,  tiles, obstacles_triangle
    character = character_class.CHARACTER()
    background = background_class.BACKGROUND()
    # obstacle.x, obstacle.y
    obstacles_triangle = [obstacle_class.OBSTACLE_TRIANGLE(i*100+i*10,115) for i in range(10)]
    # tile.x, tile.y, tile.size_x, tile.size_y, tile.mode
    # mode : 1. basic_tile  2. tile2
    tiles = [tile_class.TILE(i*100,50,100,100,1) for i in range(10)]
    global speed, isJump
    speed = 2.8
    isJump = False
    pass


def exit():
    global character, background, tiles, obstacles_triangle
    del character
    del background
    del tiles
    del obstacles_triangle
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global isJump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                # 이부분은 이후 일시정지 되도록 바꾼다 -> 추가구현 내용
                game_framework.quit()
            if event.key == SDLK_m:
                game_framework.change_state(maptool_state)
        if event.type == SDL_MOUSEBUTTONDOWN:
            isJump = True
    pass


def update():
    global isJump, speed
    background.Move(speed)
    isJump = character.Move(isJump)
    character_x, character_y = character.OutCharacterPos()
    character_size = character.OutCharacterSize()
    for obstacle in obstacles_triangle:
        obstacle.Move(speed)
        colide = obstacle.ColideCheck(character_x,character_y,character_size)
        if(colide == True):
            game_framework.change_state(title_state)
    for tile in tiles:
        tile.Move(speed)
    speed += 0.0001
    pass


def draw():
    clear_canvas()
    background.Draw()
    character.Draw()
    for obstacle in obstacles_triangle:
        obstacle.Draw()
    for tile in tiles:
        tile.Draw()
    update_canvas()
    delay(0.01)
    pass




