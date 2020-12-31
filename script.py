import pygame as pg
from pygame.locals import *
from utils import *
import numpy as np
import sys
import time

def main():
    pg.init()
    screen = pg.display.set_mode((width,height))
    player_1 = True
    table_1 = np.zeros([3,3],'float32')
    while True:
        write_table(screen)
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                positions = pg.mouse.get_pos()
                table_1,error = upgrade_table(table_1,positions,player_1)
                if not error:
                    if player_1:
                        write_x(screen,positions)
                    else:
                        write_o(screen,positions)
                    end,ganador = check(table_1,player_1)
                    if end:
                        print("Tenemos un ganador y es el jugador {}".format(ganador))
                    player_1 = not player_1
                print(table_1)
        pg.display.update()
if __name__ == "__main__":
    main()
