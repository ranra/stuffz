import pygame as pg
WIDTH, HEIGHT= 1024,  768
TILESIZE = 32
gridWidth = WIDTH / TILESIZE
gridHeight = HEIGHT / TILESIZE

LIGHT_GREY = (192,192,192)
brown = (106, 55, 5)
white=(255,255,255)
black=(0,0,0)

red=(200,0,0)
light_red=(255,0,0)

green=(34,177,76)
light_green=(0,255,0)

yellow= (200,200,0)
light_yellow= (255,255,0)
blue=(0,0,200)
light_blue=(0,0,255)
BK_COLOR = LIGHT_GREY

WALL_IMG = "tile_69.png"


#Player settings
PLAYER_IMG = "manBlue_hold.png"
PLAYER_SPEED = 50


#bomb settings

BOMB_IMG = "bomb.png"
BOMB_RADIUS = pg.Rect(0,0, 5*TILESIZE,5*TILESIZE)
BOMB_FUSE = 2000
EXPLOSION ="explosion3.png"
