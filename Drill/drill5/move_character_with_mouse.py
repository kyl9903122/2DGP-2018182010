from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
HAND_WIDTH, HAND_HEIGHT = 50,52


def handle_events():
    # fill here
    global running
    global x,y
    global character_x, character_y
    global arrow_x, arrow_y
    global delta_x, delta_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            if event.type == SDL_QUIT:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            arrow_x,arrow_y = event.x, KPU_HEIGHT -1 -event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x - HAND_WIDTH/2 , KPU_HEIGHT - 1 - event.y + HAND_HEIGHT/2
            delta_x = (x-character_x) / 100
            delta_y = (y-character_y) / 100
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    running = False

# fill here
open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
character_x, character_y = x,y
arrow_x , arrow_y =0,0
delta_x,delta_y = 0,0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if(x == character_x and y == character_y):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    else:
        character.clip_draw(0, 100 * 3, 100, 100, character_x, character_y)
    hand_arrow.clip_draw(0,0,HAND_WIDTH,HAND_HEIGHT,arrow_x,arrow_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    character_x += delta_x
    character_y += delta_y
    if((x-character_x)*(x-character_x) + (y-character_y)*(y-character_y)<16):
        character_x,character_y = x,y
        delta_x = 0
        delta_y = 0
close_canvas()




