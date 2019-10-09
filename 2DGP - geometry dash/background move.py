from pico2d import*
open_canvas(1020,510)

#init

background_1 = load_image('background1.png')
background_2 = load_image('background1.png')
background_3 = load_image('background1.png')

background_1_pivotX = 255
background_2_pivotX = 765
background_3_pivotX = 1275
backgroundPivotY = 255
speed = 1

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


while(True):
    #update
    BackgroundMove()
    UpSpeed()
    
    #render
    clear_canvas()
    BackgroundDraw(background_1_pivotX,background_2_pivotX,background_3_pivotX,backgroundPivotY)
    update_canvas()

    delay(0.01)

