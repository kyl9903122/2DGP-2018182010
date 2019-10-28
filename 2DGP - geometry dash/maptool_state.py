import game_framework
import main_state

name = "MaptoolState"

from pico2d import*





def enter():
    global mode, tile1_x, tile1_y, tile2_x,tile2_y,mode3_x, mode3_y, kind
    mode = t
    kind = 1
    tile1_x = [50,150,250,350,450]
    tile1_y = [50,50,50,50,50,50]
    global image
    image = load_image('basic_tile.png')
    global x, y, mx, my, size_x,size_y
    pass


def exit():
    # 모드를 나갈때 txt파일에 각 장애물, 타일의 pos값을 저장한다.
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global image, size_x, size_y, mx,my,x,y
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if(event.key == SDLK_t):
                mode = t
                if(kind ==1):
                    image = load_image('basic_tile.png')
                    size_x = 100
                    size_y = 100
                elif(kind == 2):
                    image = load_image('tile2.png')
                    size_x = 70
                    size_y = 20
            if event.key == SDLK_o:
                mode = o
            if(event.key == SDLK_1):
                kind = 1
                if(mode == t):
                    image = load_image('basic_tile.png')
                    size_x =100
                    size_y = 100
                elif(mode == o):
                    image = load_image('triangle_obstacle.png')
                    size_x = 40
                    size_y =40
            if event.key == SDLK_2:
                kind = 2
                if(mode == t):
                    image = load_image('tile2.png')
                    size_x = 70
                    size_y = 20
            if event.key == SDLK_3:
                kind = 3
            if event.key == SDLK_AC_BACK:
                DeleteBlock()
        if event.type == SDL_MOUSEBUTTONDOWN:
            x = event.x
            y = 510-event.y -1
            Create()
        if event.type == SDL_MOUSEMOTION:
            mx = event.x
            my = 510 - event.y -1

    pass


def update():

    pass


def draw():
    image.draw()
    pass

def Create():
    global image
    if(mode == t):
        if(kind == 1):



    pass

def DeleteBlock():
    pass