from settings import *


class Bullet(Sprite):
    sprite = pygame.image.load('sprites_objects/green_bullet.png')

    def __init__(self, parent, x, y, dx, dy):
        super().__init__(x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx, self.dy = dx, dy
        self.parent = parent

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy


class Bullet1(Bullet):
    sprite = pygame.image.load('sprites_objects/green_bullet.png')


class Bullet2(Bullet):
    sprite = pygame.image.load('sprites_objects/red_bullet.png')
