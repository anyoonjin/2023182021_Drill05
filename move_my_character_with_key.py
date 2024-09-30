from pico2d import *


open_canvas()
grass = load_image('TUK_GROUND.png')
cha = load_image('character.png')


def handle_events():
    global running ,dir1,dir2,frame_y   #dir1 좌우 dir2 상하

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                frame_y=2
                dir1-=1
            elif event.key == SDLK_RIGHT:
                frame_y=1
                dir1+=1
            elif event.key == SDLK_UP:
                frame_y=0
                dir2 +=1
            elif event.key == SDLK_DOWN:
                frame_y=3
                dir2 -=1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir1 +=1
            elif event.key == SDLK_RIGHT:
                dir1-=1
            elif event.key == SDLK_UP:
                dir2 -=1
            elif event.key == SDLK_DOWN:
                dir2 +=1


running = True
x = 800 // 2
y= 600//6
dir1 = 0
dir2 = 0
frame_x = 0
frame_y = 0 #캐릭터 방향 조정
len = 300//4

while running:
    clear_canvas()
    grass.draw(400,300)
    cha.clip_draw(frame_x*len,frame_y*len,len,len,x,y)
    update_canvas()
    handle_events()
    frame_x=(frame_x+1)%4

    if 20<=x<=780:
        x+=dir1*5
        if x>780:
            x=780
        elif x<20:
            x=20

    if 30<=y<=580:
        y+=dir2*5
        if y>580:
            y=580
        elif y<30:
            y=30
    delay(0.06)


close_canvas()
