import game_framework
import main_state

name = "MaptoolState"

from pico2d import*
import struct

import background_class
import tile_class
import obstacle_class



background = None
mode, kind = 0,0
tile_x, tile_y, tile_mode, tri_obs_x, tri_obs_y = [], [],[],[],[]
x, y, mx, my, size_x,size_y = 0,0,0,0,0,0
image = None
speed, inspeed = 0.28, 0
stop = True
tiles, tri_obses = [] , []
real_x =0
delete_idx = 0



def enter():
    global mode, kind
    mode = 't'
    kind = 1
    global basic_tile_x, basic_tile_y, tile2_x, tile2_y, tri_obs_x, tri_obs_y

    global image
    image = load_image('basic_tile.png')

    global x, y, mx, my, size_x,size_y, real_x, stop
    size_x = 100
    size_y = 100
    real_x = 0
    stop = True

    global background, speed,inspeed
    background = background_class.BACKGROUND()
    speed= 2.8
    inspeed = 0

    global tiles, tri_obses, delete_idx
    delete_idx = "tile"

    ReadPos()
    #init
    for i in range(len(tile_x)):
        if(tile_mode[i] == 1):
            tiles.append(tile_class.TILE(tile_x[i],tile_y[i],100,100,1))
        elif tile_mode[i] == 2:
            tiles.append(tile_class.TILE(tile_x[i], tile_y[i], 70, 20, 2))

    pass


def exit():
    # 모드를 나갈때 txt파일에 각 장애물, 타일의 pos값을 저장한다.
    f = open('tile_pos.txt', mode='wb')
    for i in range(len(tiles)):
        data = struct.pack('d', tile_x[i])
        f.write(data)
        data = struct.pack('d', tile_y[i])
        f.write(data)
        data = struct.pack('d', tile_mode[i])
        f.write(data)

    f2 = open('triangle_obstacle_pos.txt', mode = 'wb')
    for i in range(len(tri_obses)):
        data = struct.pack('d', tri_obs_x[i])
        f.write(data)
        data = struct.pack('d', tri_obs_y[i])
        f.write(data)

    f.close()
    f2.close()

def pause():
    pass


def resume():
    pass


def handle_events():
    global image, size_x, size_y, mx,my,x,y, inspeed, stop, mode, kind
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if(event.key == SDLK_t):
                # tile selection
                mode = 't'
                if(kind ==1):
                    image = load_image('basic_tile.png')
                    size_x = 100
                    size_y = 100
                elif(kind == 2):
                    image = load_image('tile2.png')
                    size_x = 70
                    size_y = 20
            if event.key == SDLK_o:
                # obstacle selection
                mode = 'o'
                if(kind == 1):
                    image = load_image('triangle_obstacle.png')
                    size_x = 40
                    size_y = 40
            if(event.key == SDLK_1):
                kind = 1
                if(mode == 't'):
                    image = load_image('basic_tile.png')
                    size_x =100
                    size_y = 100
                elif(mode == 'o'):
                    image = load_image('triangle_obstacle.png')
                    size_x = 40
                    size_y =40
            if event.key == SDLK_2:
                kind = 2
                if(mode == 't'):
                    image = load_image('tile2.png')
                    size_x = 70
                    size_y = 20
            if event.key == SDLK_3:
                kind = 3
            if event.key == SDLK_BACKSPACE:
                DeleteBlock()
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_s:
                inspeed = 0
                stop = True
            if event.key == SDLK_r:
                inspeed = speed
                stop = False
            if event.key == SDLK_m:
                game_framework.change_state(main_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x = event.x
            y = 510-event.y -1
            Create()
        elif event.type == SDL_MOUSEMOTION:
            mx = event.x
            my = 510 - event.y -1


    pass


def update():
    global speed, real_x, inspeed
    if(stop == False):
        background.Move(inspeed)
        speed += 0.0001
        inspeed = speed
        real_x += inspeed
        for tile in tiles:
            tile.Move(inspeed)
        for tri_obs in tri_obses:
            tri_obs.Move(inspeed)
    delay(0.01)
    pass


def draw():
    hide_cursor()
    clear_canvas()
    background.Draw()
    image.draw(mx,my,size_x,size_y)
    for tile in tiles:
        tile.Draw()
    for tri_obs in tri_obses:
        tri_obs.Draw()
    update_canvas()

    pass

def Create():
    global delete_idx
    if mode == 't' and kind == 1:
        #basic tile
        tiles.append(tile_class.TILE(x,y,size_x,size_y,1))
        tile_x.append(x+real_x)
        tile_y.append(y)
        tile_mode.append(1)
        delete_idx = "tile"
    elif mode == 't' and kind ==2:
        #tile2
        tiles.append(tile_class.TILE(x , y, size_x, size_y, 2))
        tile_x.append(x + real_x)
        tile_y.append(y)
        tile_mode.append(2)
        delete_idx = "tile"
    elif mode == 'o' and kind == 1:
        #triangle obstacle
        tri_obses.append(obstacle_class.OBSTACLE_TRIANGLE(x,y))
        tri_obs_x.append(x+real_x)
        tri_obs_y.append(y)
        delete_idx = "tri_obs"


    pass

def DeleteBlock():
    if(delete_idx =="tile"):
        del tiles[len(tiles)-1]
    if(delete_idx == "tri_obs"):
        del tri_obses[len(tri_obses)-1]
    pass

def ReadPos():
    f = open('tile_pos.txt',mode = 'rb')
    intsize = struct.calcsize('d')
    #tile pos read
    while True:
        data = f.read(intsize)
        if not data:
            break
        tile_x.append(struct.unpack('d',data))
        data = f.read(intsize)
        if not data:
            break
        tile_y.append(struct.unpack('d', data))
        data = f.read(intsize)
        if not data:
            break
        tile_mode.append(struct.unpack('d', data))



    f2 = open('triangle_obstacle_pos.txt', mode = 'rb')

    #triangle obstacle pos read
    while True:
        data = f2.read(intsize)
        if not data:
            break
        tri_obs_x.append(struct.unpack('d', data))
        data = f2.read(intsize)
        if not data:
            break
        tri_obs_y.append(struct.unpack('d', data))

    f.close()
    f2.close()
