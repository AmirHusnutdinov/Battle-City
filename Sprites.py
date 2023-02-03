from settings import *


class Cell(Sprite):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.image = load_image(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Floors(Sprite):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.image = load_image(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.rect.width < SPRITE:
            self.rect.x += (SPRITE - self.rect.width) // 2
        if self.rect.height < SPRITE:
            self.rect.y += (SPRITE - self.rect.height) // 2
        self.mask = pygame.mask.from_surface(self.image)
