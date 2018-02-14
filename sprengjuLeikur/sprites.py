import pygame as pg
from sprengjuLeikur.settings import *
vec = pg.math.Vector2
def hit_rect(a, b):
    return a.hit_rect.colliderect(b.rect)

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
            self.image = pg.transform.rotate(self.game.player_img, 180)
            self.acc.x = -PLAYER_SPEED
        if key[pg.K_RIGHT]:
            self.acc.x = PLAYER_SPEED
            self.image = pg.transform.rotate(self.game.player_img, 0)
        if key[pg.K_UP]:
            self.acc.y = -PLAYER_SPEED
            self.image = pg.transform.rotate(self.game.player_img, 90)
        if key[pg.K_DOWN]:
            self.acc.y = PLAYER_SPEED
            self.image = pg.transform.rotate(self.game.player_img, 270)
        if key[pg.K_SPACE]:
                   Bomb(self.game,self.pos.x, self.pos.y)



    def update(self):
        self.get_keys()
        self.acc += self.vel * -0.2
        self.vel += self.acc
        self.pos += (self.vel + 0.5 * self.acc) * self.game.dt
        self.rect.centerx = self.pos.x
        self.collission("x")
        self.rect.centery = self.pos.y
        self.collission("y")




    def collission(self, dir):
        collission = pg.sprite.spritecollide(self, self.game.wall_sprites, False)
        if collission:
            if dir == "x":
                if self.vel.x > 0:
                    self.pos.x = collission[0].rect.left - self.rect.width /2
                if self.vel.x < 0:
                    self.pos.x = collission[0].rect.right + self.rect.width /2
                self.rect.centerx = self.pos.x

            if dir == "y":
                if self.vel.y > 0:
                    self.pos.y = collission[0].rect.top - self.rect.height /2
                if self.vel.y < 0:
                    self.pos.y = collission[0].rect.bottom + self.rect.height /2
                self.rect.centery = self.pos.y









class Player(Person):
    def __init__(self, game, x, y, width, height, image):
        Person.__init__(self, game, x, y, width, height, image)
        self.group = game.all_sprites, game.player_sprites









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




class Bomb(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.group = game.all_sprites, game.bomb_sprites
        pg.sprite.Sprite.__init__(self,self.group)
        self.image = game.bomb_img
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.hit_rect = BOMB_RADIUS
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y
        self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y
        self.hit_rect = BOMB_RADIUS
        self.fuse = BOMB_FUSE
        self.time_planted = pg.time.get_ticks()


    def update(self):

        now = pg.time.get_ticks()
        if now > self.time_planted + self.fuse:
            pg.sprite.groupcollide(self.game.bomb_sprites, self.game.wall_sprites, False, True, hit_rect)
            self.kill()
