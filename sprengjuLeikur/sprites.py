import pygame as pg
from sprengjuLeikur.settings import *
vec = pg.math.Vector2

class Person(pg.sprite.Sprite):
    def __init__(self, game, x, y, width, height, image):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = vec(x,y) *TILESIZE
        self.pos.x = self.pos[0]
        self.pos.y = self.pos[1]
        self.rect.centerx, self.rect.centery = self.pos.x, self.pos.y
        self.rot = 0
        self.vel = vec(0, 0)
        self.acc = vec(0,0)

    def get_keys(self):
        self.acc = vec(0, 0)
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.acc.x = -PLAYER_SPEED
        if key[pg.K_RIGHT]:
            self.acc.x = PLAYER_SPEED
        if key[pg.K_UP]:
            self.acc.y = -PLAYER_SPEED
        if key[pg.K_DOWN]:
            self.acc.y = PLAYER_SPEED



    def update(self):
        self.get_keys()
        self.acc += self.vel * -0.12
        self.vel += self.acc
        self.pos += (self.vel + 0.5 * self.acc) * self.game.dt
        self.rect.center = self.pos
        self.collission()




    def collission(self):
        collission = pg.sprite.spritecollide(self, self.game.wall_sprites, False)
        if collission:
            if self.vel.x > 0:
                self.pos.x = collission[0].rect.left - self.rect.width /2
            if self.vel.x < 0:
                self.pos.x = collission[0].rect.right + self.rect.width /2
            if self.vel.y > 0:
                self.pos.y = collission[0].rect.top - self.rect.height /2
            if self.vel.y < 0:
                self.pos.y = collission[0].rect.bottom + self.rect.height /2









class Player(Person):
    def __init__(self, game, x, y, width, height, image):
        Person.__init__(self, game, x, y, width, height, image)
        self.group = game.all_sprites, game.player_sprites
        self.image.fill(green)








class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.wall_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        #self.image = pg.Surface([TILESIZE, TILESIZE])
        #self.image.fill(green)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


