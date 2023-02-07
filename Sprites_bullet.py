from settings import *


class Bullet(Sprite):
    sprite = pygame.image.load('sprites_objects/green_bullet.png')

    def __init__(self, x: int, y: int, dx: int, dy: int) -> None:
        super().__init__(x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx, self.dy = dx, dy

    def update(self) -> None:
        self.rect.x += self.dx
        self.rect.y += self.dy


class Bullet1(Bullet):
    sprite = pygame.image.load('sprites_objects/green_bullet.png')


class Bullet2(Bullet):
    sprite = pygame.image.load('sprites_objects/red_bullet.png')
