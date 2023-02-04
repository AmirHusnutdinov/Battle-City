import pygame.sprite

from Sprites import Cell, Floors
from settings import *

dict_floor = {'1': 'IndustrialTile_25.png',
              '2': 'IndustrialTile_55.png',
              '3': 'IndustrialTile_56.png',
              '5': 'IndustrialTile_64.png',
              'q': 'IndustrialTile_73.png',
              't': 'IndustrialTile_65.png',
              'd': 'IndustrialTile_66.png',
              '4': 'IndustrialTile_57.png'}
dict_wall = {'6': 'IndustrialTile_03.png',
             '7': 'IndustrialTile_12.png',
             '8': 'IndustrialTile_11.png',
             '9': 'IndustrialTile_41.png',
             'w': 'IndustrialTile_39.png',
             'e': 'IndustrialTile_29.png',
             'r': 'IndustrialTile_30.png',
             'y': 'IndustrialTile_20.png',
             'u': 'IndustrialTile_02.png',
             'i': 'IndustrialTile_19.png',
             'o': 'IndustrialTile_01.png',
             'p': 'IndustrialTile_28.png',
             'a': 'IndustrialTile_10.png',
             's': 'IndustrialTile_38.png'}


class TiledMap:

    def __init__(self, filename: list) -> None:
        self.Tank1 = None
        self.Tank2 = None
        self.pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 20, 100, 50)),
                                                      text='Pause',
                                                      manager=manager)
        self.back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((405, 300, 140, 40)),
                                                         text='Главное меню',
                                                         manager=manager)
        self.cansel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((555, 300, 140, 40)),
                                                   text='Отмена',
                                                   manager=manager)

        self.pause = pygame.image.load('data/pause.png')

        self.pause_btn.hide()
        self.back_to_menu.hide()
        self.cansel.hide()
        self.floor_layer = filename
        self.tank1_group, self.tank2_group = pygame.sprite.Group(), pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        boxes = pygame.sprite.Group()
        rows = len(self.floor_layer)
        for i in range(rows):
            for ix, value in enumerate(self.floor_layer[i]):
                if value in dict_wall.keys() or value == '@' or value == '#':
                    if value != '@' and value != '#':
                        self.all_sprites.add(Cell(ix * SPRITE, i * SPRITE, f'{dict_wall[value]}'))
                    else:
                        self.all_sprites.add(Cell(ix * SPRITE, i * SPRITE, f'{dict_wall["9"]}'))
                elif value in dict_floor.keys():
                    floor = Floors(ix * SPRITE, i * SPRITE, f'{dict_floor[value]}')
                    self.all_sprites.add(floor)
                    boxes.add(floor)
                if value == '@':
                    self.Tank1 = Tank1(ix * SPRITE, i * SPRITE)
                if value == '#':
                    self.Tank2 = Tank2(ix * SPRITE, i * SPRITE)
        if self.Tank1:
            self.all_sprites.add(self.Tank1)
            self.tank1_group.add(self.Tank1)
            self.Tank1.set_boxes(boxes, self.tank2_group)

        if self.Tank2:
            self.all_sprites.add(self.Tank2)
            self.tank2_group.add(self.Tank2)
            self.Tank2.set_boxes(boxes, self.tank1_group)

    def render(self, surf: Surface) -> None:
        image = pygame.image.load('ind_zone/Backgroundnew.png')
        surf.blit(image, (0, 0))
        self.back_to_menu.hide()
        self.cansel.hide()
        pygame.draw.rect(surf, 'black', (978, 18, 104, 54), 4, 10)

    def update(self) -> None:
        self.all_sprites.draw(screen)
        self.all_sprites.update()

    def open_pause(self, surf: Surface) -> None:
        self.back_to_menu.show()
        self.cansel.show()
        surf.blit(self.pause, (400, 200))
        pygame.draw.rect(surf, 'black', (397, 197, 307, 206), 4, 10)
        pygame.draw.rect(surf, 'black', (403, 299, 144, 43), 10, 4)
        pygame.draw.rect(surf, 'black', (553, 299, 144, 43), 10, 4)

    def on_event(self, event):
        for sprite in self.all_sprites.sprites():
            sprite.on_event(event)


class AnimatedThings:
    def __init__(self, x: int, y: int, number_of_thing=1) -> None:
        self.x = x
        self.y = y
        self.number_of_thing = number_of_thing
        self.things = []
        self.count = 0
        self.name_of_folder = None
        self.count_of_picture = 0
        if self.number_of_thing == 1:
            self.name_of_folder = 'screen1'
            self.count_of_picture = 3
        elif self.number_of_thing == 2:
            self.name_of_folder = 'screen2'
            self.count_of_picture = 3
        elif self.number_of_thing == 3:
            self.name_of_folder = 'transformater'
            self.count_of_picture = 3
        elif self.number_of_thing == 4:
            self.name_of_folder = 'hummer'
            self.count_of_picture = 5

        self.items = (os.listdir(f'{os.path.abspath(f"ind_zone/animated_things/{self.name_of_folder}")}'))
        for i in range(len(self.items)):
            self.things.append(pygame.image.load(f'ind_zone/animated_things/{self.name_of_folder}/{self.items[i]}'))

    def render(self) -> None:
        screen.blit(self.things[self.count], (self.x, self.y))
        if int(self.count) < int(self.count_of_picture):
            self.count += 1
        else:
            self.count = 0


class Tank1(Sprite):
    sprite = load_image('../hero/all_tank1.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        self.normal = 0
        self.cur_frame = 0
        self.is_move = False
        self.direction = None
        self.frames = []
        self.is_shot = False
        self.bullets = pygame.sprite.Group()
        self.rect = pygame.Rect(x, y, 32, 32)
        for i in range(12):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(self.sprite.subsurface(pygame.Rect(frame_location, self.rect.size)))
        self.update_frame()
        self.shotTimer = 0
        self.shotDelay = 50

    def update_frame(self):
        if not self.is_move:
            self.image = self.frames[self.cur_frame]
            self.mask = pygame.mask.from_surface(self.image)
            return
        elif self.direction == pygame.K_LEFT:
            self.normal = 3
        elif self.direction == pygame.K_RIGHT:
            self.normal = 9
        elif self.direction == pygame.K_UP:
            self.normal = 6
        elif self.direction == pygame.K_DOWN:
            self.normal = 0
        if self.cur_frame > self.normal:
            self.cur_frame -= 1
        elif self.cur_frame < self.normal:
            self.cur_frame += 1
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)

    def set_boxes(self, boxes: pygame.sprite.Group, tank_group):
        self.boxes = boxes
        self.tank_group = tank_group

    def move(self, x: int, y: int):
        old_x = self.rect.x
        old_y = self.rect.y
        if x < 0 or y < 0:
            return
        if x + self.rect.width > WIDTH or y + self.rect.height > HEIGHT:
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

    def check_hit(self):
        booms = [pygame.image.load('hero/hero_stay/normal/взрыв4.png')]

        for box in self.boxes.sprites():
            for bull in self.bullets.sprites():
                if pygame.sprite.collide_mask(box, bull):
                    x = box.rect.x
                    y = box.rect.y
                    for i in booms:
                        rect = i.get_rect(bottomright=(x + 32, y + 32))
                        screen.blit(i, rect)
                    pygame.sprite.spritecollide(box, self.bullets, True)

        for i in self.bullets.sprites():
            for j in self.tank_group:
                if pygame.sprite.collide_mask(i, j):
                    print('tank2 kill!!!')
                    pygame.sprite.spritecollide(j, self.bullets, True)

    def update(self, *args, **kwargs):
        if self.is_shot and self.shotTimer == 0:
            if self.side == 1:
                self.bullets.add(Bullet1(self, self.rect.x, self.rect.y, -10, 0))
            if self.side == 3:
                self.bullets.add(Bullet1(self, self.rect.x, self.rect.y, 10, 0))
            if self.side == 2:
                self.bullets.add(Bullet1(self, self.rect.x, self.rect.y, 0, -10))
            if self.side == 4:
                self.bullets.add(Bullet1(self, self.rect.x, self.rect.y, 0, 10))
            self.shotTimer = self.shotDelay
        self.bullets.draw(screen)
        self.bullets.update()
        self.check_hit()
        self.update_frame()
        step = 5
        if self.is_move:
            if self.direction == pygame.K_LEFT:
                self.move(self.rect.x - step, self.rect.y)
            if self.direction == pygame.K_RIGHT:
                self.move(self.rect.x + step, self.rect.y)
            if self.direction == pygame.K_UP:
                self.move(self.rect.x, self.rect.y - step)
            if self.direction == pygame.K_DOWN:
                self.move(self.rect.x, self.rect.y + step)

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.KEYUP:
            self.is_move = False
            self.direction = False
            self.is_shot = False
        if self.shotTimer > 0:
            self.shotTimer -= 1
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            self.is_move = True
            self.direction = event.key
            if event.key == pygame.K_LEFT:
                self.side = 1
            elif event.key == pygame.K_DOWN:
                self.side = 4
            elif event.key == pygame.K_RIGHT:
                self.side = 3
            elif event.key == pygame.K_UP:
                self.side = 2
        if event.key == pygame.K_RCTRL:
            self.is_shot = True


class Tank2(Sprite):
    sprite = load_image('../hero/all_tank2.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        self.normal = 0
        self.cur_frame = 0
        self.is_move = False
        self.direction = None
        self.frames = []
        self.is_shot = False
        self.bullets = pygame.sprite.Group()
        self.rect = pygame.Rect(x, y, 32, 32)
        for i in range(12):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(self.sprite.subsurface(pygame.Rect(frame_location, self.rect.size)))
        self.update_frame()
        self.shotTimer = 0
        self.shotDelay = 50
        self.side = 4

    def update_frame(self):
        if not self.is_move:
            self.image = self.frames[self.cur_frame]
            self.mask = pygame.mask.from_surface(self.image)
            return
        elif self.direction == pygame.K_a:
            self.normal = 3
        elif self.direction == pygame.K_d:
            self.normal = 9
        elif self.direction == pygame.K_w:
            self.normal = 6
        elif self.direction == pygame.K_s:
            self.normal = 0
        if self.cur_frame > self.normal:
            self.cur_frame -= 1
        elif self.cur_frame < self.normal:
            self.cur_frame += 1
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)

    def set_boxes(self, boxes: pygame.sprite.Group, tank_group):
        self.boxes = boxes
        self.tank_group = tank_group

    def move(self, x: int, y: int):
        old_x = self.rect.x
        old_y = self.rect.y
        if x < 0 or y < 0:
            return
        if x + self.rect.width > WIDTH or y + self.rect.height > HEIGHT:
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

    def check_hit(self):
        booms = [pygame.image.load('hero/hero_stay/normal/взрыв4.png')]

        for box in self.boxes.sprites():
            for bull in self.bullets.sprites():
                if pygame.sprite.collide_mask(box, bull):
                    x = box.rect.x
                    y = box.rect.y
                    pygame.sprite.spritecollide(box, self.bullets, True)
                    for i in booms:
                        rect = i.get_rect(bottomright=(x + 32, y + 32))
                        screen.blit(i, rect)
        for i in self.bullets.sprites():
            for j in self.tank_group:
                if pygame.sprite.collide_mask(i, j):
                    print('tank1 kill!!!')
                    pygame.sprite.spritecollide(j, self.bullets, True)

    def update(self, *args, **kwargs):
        if self.is_shot and self.shotTimer == 0:
            if self.side == 1:
                self.bullets.add(Bullet2(self, self.rect.x, self.rect.y, -10, 0))
            if self.side == 3:
                self.bullets.add(Bullet2(self, self.rect.x, self.rect.y, 10, 0))
            if self.side == 2:
                self.bullets.add(Bullet2(self, self.rect.x, self.rect.y, 0, -10))
            if self.side == 4:
                self.bullets.add(Bullet2(self, self.rect.x, self.rect.y, 0, 10))
            self.shotTimer = self.shotDelay
        self.bullets.draw(screen)
        self.bullets.update()
        self.check_hit()

        self.update_frame()
        step = 5
        if self.is_move:
            if self.direction == pygame.K_a:
                self.move(self.rect.x - step, self.rect.y)
            if self.direction == pygame.K_d:
                self.move(self.rect.x + step, self.rect.y)
            if self.direction == pygame.K_w:
                self.move(self.rect.x, self.rect.y - step)
            if self.direction == pygame.K_s:
                self.move(self.rect.x, self.rect.y + step)

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.KEYUP:
            self.is_move = False
            self.direction = False
            self.is_shot = False
        if self.shotTimer > 0:
            self.shotTimer -= 1
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]:
            self.is_move = True
            self.direction = event.key
            if event.key == pygame.K_a:
                self.side = 1
            elif event.key == pygame.K_s:
                self.side = 4
            elif event.key == pygame.K_d:
                self.side = 3
            elif event.key == pygame.K_w:
                self.side = 2
        if event.key == pygame.K_q:
            self.is_shot = True


class Bullet1(Sprite):
    sprite = pygame.image.load('./hero/hero_stay/normal/зеленый_снаряд1.png')

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


class Bullet2(Sprite):
    sprite = pygame.image.load('./hero/hero_stay/normal/красный_снаряд1.png')

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
