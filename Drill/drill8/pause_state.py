import game_framework
import main_state
from pico2d import*

def enter():
    global image
    image = load_image('title.png')
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
    image.draw(400, 300,400,300)
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass