from settings import *


class Sprite(pygame.sprite.Sprite):
    sprite = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = self.__class__.sprite
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


class Hero(Sprite):
    sprite = pygame.image.load('hero/1-PhotoRoom.png-PhotoRoom.png')
    
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.all_sprites = pygame.sprite.Group()
        self.is_move = False
        self.direction = None
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("hero/1-PhotoRoom.png-PhotoRoom.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = 55
        self.sprite.rect.y = 190

    def set_boxes(self, boxes: pygame.sprite.Group):
        self.boxes = boxes

    def move(self, x, y):
        print(123)
        old_x = self.rect.x
        old_y = self.rect.y
        if x < 0 or y < 0:
            return
        if x + self.rect.width < WIDTH or y + self.rect.height > HEIGHT:
            return
        self.rect.x = x
        self.rect.y = y
        if not self.boxes:
            return
        for box in self.boxes.sprites():
            if pygame.sprite.collide_mask(self, box):
                self.rect.x = old_x
                self.rect.y = old_y
                return

    def update(self, *args, **kwargs) -> None:
        if not self.is_move:
            return
        step = 5
        if self.direction == pygame.K_LEFT:
            self.move(self.rect.x - step, self.rect.y)
        if self.direction == pygame.K_RIGHT:
            self.move(self.rect.x + step, self.rect.y)

    def on_event(self, event):
        if event.type == pygame.KEYUP:
            self.is_move = False
            self.direction = False
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            self.is_move = True
            self.direction = event.key

