from pico2d import*
import  math
open_canvas(1020,510)

TILESIZE = 100
TILECNT = 100
CHARACTERSIZE = 60
#init

background_1 = load_image('background1.png')
background_2 = load_image('background1.png')
background_3 = load_image('background1.png')
basic_tile = load_image('basic_tile.png')
character = load_image('character.png')

background_1_pivotX = 255
background_2_pivotX = 765
background_3_pivotX = 1275
backgroundPivotY = 255
speed = 1
character_jump =False

def handle_events():
    global running
    global character_jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDL_ESCAPE:
                # 이부분은 이후 일시정지 되도록 바꾼다 -> 추가구현 내용
                running = False
        if event.type == SDL_MOUSEBUTTONDOWN:
            character_jump = True

def BackgroundMove():
    global background_1_pivotX
    global background_2_pivotX
    global background_3_pivotX
    global speed
    if(background_1_pivotX<=-255):
        background_1_pivotX = background_3_pivotX+510
    if(background_2_pivotX<=-255):
        background_2_pivotX = background_1_pivotX+510
    if(background_3_pivotX<=-255):
        background_3_pivotX = background_2_pivotX+510
    background_1_pivotX -= speed    
    background_2_pivotX -= speed
    background_3_pivotX -= speed
   

def BackgroundDraw(bk1_pivot_x,bk2_pivot_x,bk3_pivot_x,bk_pivot_y):
    background_1.clip_draw(0,0,512,512,bk1_pivot_x,bk_pivot_y,512,512)
    background_2.clip_draw(0,0,512,512,bk2_pivot_x,bk_pivot_y,512,512)
    background_2.clip_draw(0,0,512,512,bk3_pivot_x,bk_pivot_y,512,512)
    
def UpSpeed():
    global speed
    speed += 0.0001

def InitMap():
    #초기 단계이므로 일단 타일만 깐다
    global basic_tiles_x, basic_tiles_y # tiles pivot value
    basic_tiles_x = [n*100 + TILESIZE/2 for n in range(0,TILECNT)]
    basic_tiles_y = [50 for n in range(0,TILECNT)]

def TilesMove():
    for i in range(0,TILECNT):
        basic_tiles_x[i] -= speed

def DrawTiles():
    for i in range(0,TILECNT):
        if(basic_tiles_x[i]>=-50 and basic_tiles_x[i]<=1070):
            basic_tile.draw(basic_tiles_x[i],basic_tiles_y[i])

def MoveCharacter():
    global character_x, character_y
    global degree
    if(character_jump == True):
        character_y += math.sin(degree/360 *2 *math.pi) * 10
    degree+=5




running = True
basic_tiles_x = [0 for n in range(0, TILECNT)]
basic_tiles_y = [50 for n in range(0, TILECNT)]
character_x, character_y = 130, 130

degree = 0

InitMap()
while(running):
    handle_events()
    #update
    BackgroundMove()
    UpSpeed()
    TilesMove()
    MoveCharacter()
    if (character_y<130):
        degree = 0
        character_y = 130
        character_jump = False
    #draw
    clear_canvas()
    BackgroundDraw(background_1_pivotX,background_2_pivotX,background_3_pivotX,backgroundPivotY)
    DrawTiles()
    character.clip_draw(0,0,117,118,character_x,character_y,CHARACTERSIZE,CHARACTERSIZE)
    update_canvas()


    delay(0.01)

