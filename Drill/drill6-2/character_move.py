from pico2d import*
import random

KPU_WIDTH, KPU_HEIGHT = 1280,1024

vertex_x = [random.randint(200,1000) for n in range(10)]
vertex_y = [random.randint(200,800) for n in range(10)]
open_canvas(KPU_WIDTH,KPU_HEIGHT)
character = load_image('animation_sheet.png')
background = load_image('KPU_GROUND.png')
character_frame_x,character_frame_y = 0,0
character_dir = 0 # 0-> left, 1-> right
character_x , character_y = vertex_x[0],vertex_y[0]
n  = 0
while True:
    for i in range(0,50):
        t = i / 100
        character_x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        character_y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x, y))
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if (vertex_x[n + 1] < vertex_x[n]):
            character.clip_draw(character_frame_x * 100, 100, 100, 100, character_x, character_y)
        else:
            character.clip_draw(character_frame_x * 100, 0, 100, 100, character_x, character_y)
        update_canvas()
        handle_events()
        character_frame_x = (character_frame_x + 1) % 8
        delay(0.03)
    n=(n+1)%10

    for n in range(1,7):
        for i in range(0,100):
            t = i / 100
            character_x = ((-t ** 3 + 2 * t ** 2 - t) * character_x[n-1] + (3 * t ** 3 - 5 * t ** 2 + 2) * character_x[n] + (-3 * t ** 3 + 4 * t ** 2 + t) * character_x[n+1] + (t ** 3 - t ** 2) * character_x[n+2]) / 2
            character_y = ((-t ** 3 + 2 * t ** 2 - t) * character_y[n-1] + (3 * t ** 3 - 5 * t ** 2 + 2) * character_y[n] + (-3 * t ** 3 + 4 * t ** 2 + t) * character_y[n+1] + (t ** 3 - t ** 2) * character_y[n+2]) / 2
            draw_point((x, y))
            background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            if (vertex_x[n + 1] < vertex_x[n]):
                character.clip_draw(character_frame_x * 100, 100, 100, 100, character_x, character_y)
            else:
                character.clip_draw(character_frame_x * 100, 0, 100, 100, character_x, character_y)
            update_canvas()
            handle_events()
            character_frame_x = (character_frame_x + 1) % 8
            delay(0.03)
        n = (n + 1) % 10

    for n in range(7,9):
        t = i / 100
        character_x = ((-t ** 3 + 2 * t ** 2 - t) * character_x[n-1] + (3 * t ** 3 - 5 * t ** 2 + 2) * character_x[n] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * character_x[(n+1)%10] + (t ** 3 - t ** 2) * character_x[(n+2)%10]) / 2
        character_y = ((-t ** 3 + 2 * t ** 2 - t) * character_y[n-1] + (3 * t ** 3 - 5 * t ** 2 + 2) * character_y[n] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * character_y[(n+1)%10] + (t ** 3 - t ** 2) * character_y[(n+2)%10]) / 2
        draw_point((x, y))
        background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if (vertex_x[n + 1] < vertex_x[n]):
            character.clip_draw(character_frame_x * 100, 100, 100, 100, character_x, character_y)
        else:
            character.clip_draw(character_frame_x * 100, 0, 100, 100, character_x, character_y)
        update_canvas()
        handle_events()
        character_frame_x = (character_frame_x + 1) % 8
        delay(0.03)
    n = (n + 1) % 10
