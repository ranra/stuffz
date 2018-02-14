import pygame as pg
sheet = "../sprites/bombsheet"
r = 8
col = 9

pg.init()
screen = pg.display.set_mode((800, 800))
class Spritesheet():
    def __init__(self, rows, col, file):
        self.file = pg.image.load(file)
        self.rect = self.file.get_rect()
        self.rows = rows
        self.col = col
        self.total = col * rows
        w = self.sprite_width = self.rect.width/col
        h = self.sprite_height = self.rect.height/rows
        self.list = list([(i%self.col,i/rows,w,h) for i in range(self.total)])
    def draw(self,index, x, y):
        pg.Surface.blit(self.file,(x, y), self.list[index])




index = 0
s = Spritesheet(r, col, sheet)
def loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    s.draw(index % s.total, 400,400)
    index +=1

loop()
