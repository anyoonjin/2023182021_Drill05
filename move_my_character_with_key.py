from pico2d import *


open_canvas()
grass = load_image('TUK_GROUND.png')
cha = load_image('character.png')


def handle_events():
    global running
    global x
    global y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                x-=10
            elif event.key == SDLK_RIGHT:
                x+=10
            elif event.key == SDLK_UP:
                y+=10
            elif event.key == SDLK_DOWN:
                y-=10
        # fill here


running = True
x = 800 // 2
y=600//2
frame = 0

while running:
    clear_canvas()
    grass.draw(400,300)
    cha.clip_draw(frame*80,80,80,80,x,y)
    update_canvas()
    handle_events()
    frame=(frame+1)%4
    delay(0.07)


close_canvas()
