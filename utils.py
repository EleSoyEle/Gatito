import pygame as pg
import numpy as np

width = 500
height = 500
size = width//3

def upgrade_table(table,positions,player_1):
    new_table = np.copy(table)
    mtps = []
    for i in range(2):
        dif = positions[i] % size
        mtps.append(positions[i] - dif)
    pos_x = mtps[0]//size
    pos_y = mtps[1]//size

    print(pos_x,pos_y)
    error = False
    if player_1:
        if new_table[pos_x,pos_y] == 0:
            new_table[pos_x,pos_y] = 1
        else:
            error = True
    else:
        if new_table[pos_x,pos_y] == 0:
            new_table[pos_x,pos_y] = 2
        else:
            error = True

    return new_table,error

def check(table,player_1):
    ganador = False
    n = 1 if player_1 else 2
    for i in range(3):
        if table[i,1] == n:
            if table[i,0] == n and table[i,2] == n:
                ganador = True
                return ganador,n

        if table[1,i] == n:
            if table[0,i] == n and table[2,i] == n:
                ganador = True
                return ganador,n
    if table[1,1] == n:
        if table[0,0] == n and table[2,2] == n:
            ganador = True
            return ganador,n
        if table[0,2] == n and table[2,0] == n:
            ganador = True
            return ganador,n
    return False,0

def write_o(screen,positions):
    pg.draw.circle(screen,[255,255,255],positions,size//5,3)

def write_x(screen,positions):
    a = 5
    pg.draw.line(screen,[255,255,255],[positions[0]-size//a,positions[1]-size//a],[positions[0]+size//a,positions[1]+size//a],5)
    pg.draw.line(screen,[255,255,255],[positions[0]-size//a,positions[1]+size//a],[positions[0]+size//a,positions[1]-size//a],5)

def write_table(screen):
    pg.draw.rect(screen,[255,255,255],[0,size,width-5,10])
    pg.draw.rect(screen,[255,255,255],[0,size*2,width-5,10])

    pg.draw.rect(screen,[255,255,255],[size,0,10,width-5])
    pg.draw.rect(screen,[255,255,255],[size*2,0,10,width-5])

def clear_screen(screen):
    pg.draw.rect(screen,[0,0,0],(0,0,500,500))
