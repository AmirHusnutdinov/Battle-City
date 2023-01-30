from settings import *
from Map import TiledMap

class Hero(Sprite):
    sprite = pygame.image.load('hero/hero_stay/i1.png')

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.all_sprites = pygame.sprite.Group()
        self.is_move = False
        self.direction = None
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("hero/hero_stay/normal/i1.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = 55
        self.sprite.rect.y = 190
        self.mode_hero = None
        self.map = TiledMap(level_map)

    def move(self, x: int, y: int):
        old_x = self.rect.x
        old_y = self.rect.y
        if x < 0 or y < 0:
            return
        if x + self.rect.width < WIDTH or y + self.rect.height > HEIGHT:
            return
        self.rect.x = x
        self.rect.y = y
        groups = [self.map.boxes, self.map.kill, self.map.win, self.map.ladders]

        for i in groups:
            for j in i:
                if pygame.sprite.collide_mask(self, j) and i == self.map.boxes:
                    self.rect.x = old_x
                    self.rect.y = old_y
                    return
                elif pygame.sprite.collide_mask(self, j) and i == self.map.ladders:
                    self.mode_hero = 'climb'
                elif pygame.sprite.collide_mask(self, j) and i == self.map.kill:
                    mode = 'death'
                    return mode
                elif pygame.sprite.collide_mask(self, j) and i == self.map.win:
                    mode = 'win'
                    return mode

    def update(self, *args, **kwargs):
        if not self.is_move:
            return
        step = 5
        if self.direction == pygame.K_LEFT:
            self.move(self.rect.x - step, self.rect.y)
        if self.direction == pygame.K_RIGHT:
            self.move(self.rect.x + step, self.rect.y)

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.KEYUP:
            self.is_move = False
            self.direction = False
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            self.is_move = True
            self.direction = event.key

