import game_framework
import main_state
from pico2d import*

icon_time = 0

def enter():
    global image, icon_time
    image = load_image('pause.png')
    icon_time = 1
    pass



def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN:
                    if event.key == SDLK_ESCAPE:
                        game_framework.quit()
                    if event.key == SDLK_p:
                        game_framework.pop_state()
            pass


def draw():
    clear_canvas()
    main_state.draw()
    if(icon_time%2) == 0:
        image.draw(400, 300,400,300)
    update_canvas()
    pass


def update():
    global icon_time
    icon_time += 1
    if(icon_time>2):
        delay(0.5)
    pass


def pause():
    pass


def resume():
    pass