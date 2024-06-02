import time
import pygame as pg
def main():
    counter=0
    pg.init()
    stop_game = False
    display = pg.display.set_mode((600, 600))
    pg.display.set_caption('War Of The Ships')
    pg.mixer.music.load("Dada Life - Tonight Were Kids Again.mp3")
    pg.mixer.music.set_volume(0.12)
    pg.mixer.music.play()
    timer=time.time()
    welcom_img = pg.image.load("welcome page.png")
    display.blit(welcom_img, (0,0))
    pg.display.update()
    time.sleep(2)
    pg.display.update()
    second_message = pg.image.load("second message.png")
    display.blit(second_message, (0, 0))
    pg.display.update()
    time.sleep(3.5)
    first_message = pg.image.load("white starts.png")
    display.blit(first_message, (0, 0))
    pg.display.update()
    time.sleep(3.5)
    start_pos_line=[(0,120),(0,240),(0,360),(0,480),(120,0),(240,0),(360,0),(480,0)]
    end_pos_line=[(600,120),(600,240),(600,360),(600,480),(120,600),(240,600),(360,600),(480,600)]
    black_squer_pos=[(0,0),(0,480),(480,0),(480,480)]
    white_ships_pos=[(120,0),(240,0),(360,0)]
    black_ships_pos=[(0,120),(0,240),(0,360)]
    game_board=[
        ['*','w','w','w','*'],
        ['b','','','',''],
        ['b','','','',''],
        ['b','','','',''],
        ['*','','','','*']
    ]
    white_ship=pg.image.load("ship1.png")
    black_ship=pg.image.load("ship2.png")
    while not stop_game:
        ne_time=int(time.time()-timer)
        if ne_time%145==0:
            pg.mixer.music.load("Dada Life - Tonight Were Kids Again.mp3")
            pg.mixer.music.set_volume(0.12)
            pg.mixer.music.play()
        display.fill((240,230,140))
        for w_pos,b_pos in zip(white_ships_pos,black_ships_pos):
            display.blit(white_ship,w_pos)
            display.blit(black_ship,b_pos)
        for i in range(8):
            pg.draw.line(display,(0,0,255),start_pos_line[i],end_pos_line[i],2)
        for squer in black_squer_pos:
            pg.draw.rect(display,(0,0,0),(squer,(120,120)),0)
        pg.display.update()
        pg.time.Clock().tick(30)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                stop_game=True
                pg.quit()
            if event.type==pg.MOUSEBUTTONDOWN:
                mouse_x=event.pos[0]//120
                mouse_y=event.pos[1]//120
                if valid_move(mouse_x,mouse_y,game_board,counter)=='w1':
                    game_board[mouse_y][mouse_x],game_board[mouse_y+1][mouse_x]='','w'
                    white_ships_pos[mouse_x-1]=(mouse_x*120,(mouse_y+1)*120)
                    counter += 1
                elif valid_move(mouse_x,mouse_y,game_board,counter)=='w2':
                    game_board[mouse_y][mouse_x], game_board[mouse_y + 2][mouse_x] = '', 'w'
                    white_ships_pos[mouse_x-1] = (mouse_x * 120, (mouse_y + 2) * 120)
                    counter += 1
                elif valid_move(mouse_x,mouse_y,game_board,counter)=='b1':
                    game_board[mouse_y][mouse_x], game_board[mouse_y][mouse_x+1] = '', 'b'
                    black_ships_pos[mouse_y-1]=((mouse_x+1)*120,mouse_y*120)
                    counter += 1
                elif valid_move(mouse_x,mouse_y,game_board,counter)=='b2':
                    game_board[mouse_y][mouse_x], game_board[mouse_y][mouse_x+2] = '', 'b'
                    black_ships_pos[mouse_y-1] = ((mouse_x + 2) * 120, mouse_y * 120)
                    counter+=1
                if counter%2==0 and True not in is_any_move(white_ships_pos,game_board,counter):
                    counter+=1
                    no_move=pg.image.load("white no move.png")
                    display.blit(no_move,(0,0))
                    pg.display.update()
                    time.sleep(2)
                    next_turn=pg.image.load("next turn.png")
                    display.blit(next_turn,(0,0))
                    pg.display.update()
                    time.sleep(2)
                elif counter%2==1 and True not in is_any_move(black_ships_pos,game_board,counter):
                    counter += 1
                    no_move = pg.image.load("black no move.png")
                    display.blit(no_move, (0, 0))
                    pg.display.update()
                    time.sleep(2)
                    next_turn = pg.image.load("next turn.png")
                    display.blit(next_turn, (0, 0))
                    pg.display.update()
                    time.sleep(2)
        if game_board[-1]==['*','w','w','w','*']:
            last_message = pg.image.load("white wins.png")
            display.blit(last_message, (0, 0))
            pg.display.update()
            time.sleep(3)
            stop_game = True
            pg.quit()
        elif game_board[1][-1]==game_board[2][-1]==game_board[3][-1]=='b':
            last_message=pg.image.load("balck wins.png")
            display.blit(last_message,(0,0))
            pg.display.update()
            time.sleep(3)
            stop_game=True
            pg.quit()
def valid_move(x,y,game_board,counter):
    if counter%2==0 and y<4 and game_board[y][x]=='w' and game_board[y+1][x]=='':
        return 'w1'
    if counter%2==0 and y<3 and game_board[y][x]=='w' and game_board[y+2][x]=='':
        return 'w2'
    if counter%2==1 and x<4 and game_board[y][x]=='b' and game_board[y][x+1]=='':
        return 'b1'
    if counter%2==1 and x<3 and game_board[y][x]=='b' and game_board[y][x+2]=='':
        return 'b2'
    return False
def is_any_move(ship_pose,game_board,counter):
    result=[]
    for item in ship_pose:
        if valid_move(item[0]//120,item[1]//120,game_board,counter)!=False:
            result.append(True)
        else:
            result.append(False)
    return result
if __name__=="__main__":
    main()