import pygame as pg
from os import path
from sprengjuLeikur.settings import *
from sprengjuLeikur.sprites import *
from sprengjuLeikur.map import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()


    def new(self):
        game_folder = path.dirname(__file__)
        self.wall_folder = path.join(game_folder, "../sprites/PNG/Tiles")
        self.map = Map(path.join(game_folder, "map.txt"))
        self.wall_img = pg.image.load(path.join(self.wall_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

        self.all_sprites = pg.sprite.Group()
        self.wall_sprites = pg.sprite.Group()
        self.player_sprites = pg.sprite.Group()


        for row, tiles in enumerate(self.map.map_data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "P":
                    self.player = Player(self, 10, 10, 10, 10, pg.Surface([TILESIZE, TILESIZE]))


    def draw(self):
        self.screen.fill(BK_COLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000
            self.event()
            self.update()
            self.draw()





    def update(self):
        self.all_sprites.update()



    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()


g = Game()
def loop():
    g.new()
    g.run()
loop()