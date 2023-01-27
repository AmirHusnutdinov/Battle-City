from settings import *


class Hero:
    def __init__(self) -> None:
        self.sprite = pygame.image.load('Hero/p1.png')
        self.is_move = False
        self.direction = 'right'
        self.move = 20

    def render(self, surf: Surface) -> None:
        surf.blit(self.sprite, (self.move, 390))
