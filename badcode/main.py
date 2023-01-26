import pygame
import pygame_gui
import pytmx
from pygame import Surface

import os
import random

FPS = 50
shift_of_map = 0

pygame.init()
pygame.display.set_caption('Great way')
size = (1100, 600)
screen = pygame.display.set_mode(size)

manager = pygame_gui.UIManager((1100, 600))
clock = pygame.time.Clock()
running = True
mode = 'main'


class StartPage:
    def __init__(self) -> None:
        self.backgrounds_lst = []
        self.position = 0
        self.last_im = None
        self.graffiti = None
        self.coordinates = []
        self.pict = None
        self.graf = None
        self.backgrounds = (os.listdir(f'{os.path.abspath("../BackGrounds")}'))

        for i in self.backgrounds:
            self.backgrounds_lst.append(pygame.image.load(f'BackGrounds/{i}'))

        self.image = self.backgrounds_lst[random.randrange(0, len(self.backgrounds_lst))]

        self.choose_level = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=['Industrial Zone', 'Green Zone'],
            starting_option='Industrial Zone',
            relative_rect=pygame.Rect(300, 275, 150, 50),
            manager=manager)

        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (150, 60)),
                                                      text='Start',
                                                      tool_tip_text='Старт уровня игры',
                                                      manager=manager)

        self.rule_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 275), (150, 50)),
                                                     text='Rules',
                                                     tool_tip_text='Откроет правилила игры',
                                                     manager=manager)

    def render_back(self, surf: Surface) -> None:

        surf.blit(self.image, (self.position, 0))

        if self.position > - 100:
            self.position -= FPS * clock.tick(60) / 1000

        else:
            self.last_im = self.image
            self.image = self.backgrounds_lst[random.randrange(0, len(self.backgrounds_lst))]

            while self.image == self.last_im:
                self.image = self.backgrounds_lst[random.randrange(0, len(self.backgrounds_lst))]

            self.position = random.randrange(-5, 2)

    def render_front(self, surf: Surface) -> None:

        pygame.draw.rect(surf, (255, random.randrange(1, 256), random.randrange(1, 256)),
                         (498, 273, 155, 65), 10, 10)
        pygame.draw.rect(surf, 'grey', (698, 273, 155, 55), 10, 10)
        pygame.draw.rect(surf, 'grey', (298, 273, 155, 55), 10, 10)
        rules.back_btn.hide()

        self.graffiti = (os.listdir(f'{os.path.abspath("../graffiti")}'))
        self.coordinates = [(300, 500), (700, 500), (150, 400),
                            (500, 450), (900, 100), (300, 150),
                            (960, 300), (600, 100), (980, 500),
                            (300, 440), (700, 250)]

        for i in range(len(self.graffiti)):
            self.pict = pygame.image.load(f'graffiti/{self.graffiti[i]}')
            self.graf = self.pict.get_rect(bottomright=(self.coordinates[i]))
            surf.blit(self.pict, self.graf)

        self.start_btn.show()
        self.rule_btn.show()
        self.choose_level.show()

        industrial_zone.cansel.hide()
        industrial_zone.pause_btn.hide()
        industrial_zone.back_to_menu.hide()


class ConfirmationDialog:
    def __init__(self) -> None:
        self.confirmation_dialog1 = None

    def open_confirmation_dialog(self) -> None:
        self.confirmation_dialog1 = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect((400, 100), (300, 200)),
            manager=manager,
            window_title='Confirm',
            action_long_desc='Вы уверены, что хотите выйти ?',
            action_short_name='YES',
            blocking=True)


class Rules:
    def __init__(self) -> None:
        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((930, 20), (150, 50)),
                                                     text='Come back',
                                                     tool_tip_text='Press this Button!',
                                                     manager=manager)

    def render(self, surf: Surface) -> None:
        self.back_btn.show()

        start_page.start_btn.hide()
        start_page.rule_btn.hide()
        start_page.choose_level.hide()

        pict2 = pygame.image.load('../rules.png')
        graf2 = pict2.get_rect(bottomright=(1100, 600))
        surf.blit(pict2, graf2)


class TiledMap:
    def __init__(self, filename: str) -> None:
        tm = pytmx.load_pygame(filename, pixelalpha=True)

        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmx_data = tm

        self.pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 20, 100, 50)),
                                                      text='Pause',
                                                      manager=manager)
        self.back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((405, 300, 140, 40)),
                                                         text='Главное меню',
                                                         manager=manager)
        self.cansel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((555, 300, 140, 40)),
                                                   text='Отмена',
                                                   manager=manager)
        self.pause = pygame.image.load('../pause.png')

        self.pause_btn.hide()
        self.back_to_menu.hide()
        self.cansel.hide()

        self.all_sprites = pygame.sprite.Group()
        boxes = pygame.sprite.Group()
        self.hero = None

    def render(self, surf: Surface, shift: float) -> None:
        image = pygame.image.load('../ind_zone/Background_new.png')

        surf.blit(image, (0, 0))
        surf.blit(image, (1067, 0))

        ti = self.tmx_data.get_tile_image_by_gid

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    x += shift
                    if tile:
                        surf.blit(tile, (x * self.tmx_data.tilewidth,
                                         y * self.tmx_data.tileheight))

        self.back_to_menu.hide()
        self.cansel.hide()
        start_page.rule_btn.hide()
        start_page.choose_level.hide()
        start_page.start_btn.hide()

        industrial_zone.pause_btn.show()
        pygame.draw.rect(surf, 'black', (978, 18, 104, 54), 4, 10)

    def open_pause(self, surf: Surface) -> None:

        self.back_to_menu.show()
        self.cansel.show()

        surf.blit(self.pause, (400, 200))

        pygame.draw.rect(surf, 'black', (397, 197, 307, 206), 4, 10)
        pygame.draw.rect(surf, 'black', (403, 299, 144, 43), 10, 4)
        pygame.draw.rect(surf, 'black', (553, 299, 144, 43), 10, 4)


class Sprite(pygame.sprite.Sprite):
    sprite = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = self.__class__.sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.rect.width < 32:
            self.rect.x += (32 - self.rect.width) // 2
        if self.rect.height < 32:
            self.rect.y += (32 - self.rect.height) // 2
        self.mask = pygame.mask.from_surface(self.image)

    def on_event(self, event):
        pass


class Hero(Sprite):
    sprite = pygame.image.load('../hero/p1.png')

    def set_boxes(self, boxes: pygame.sprite.Group):
        self.boxes = boxes

    def move(self, x, y):
        old_x = self.rect.x
        old_y = self.rect.y
        if x < 0 or y < 0:
            return
        if x + self.rect.width > 1100 or old_y + self.rect.height > 600:
            return
        self.rect.x = x
        self.rect.y = y
        for box in self.boxes.sprites():
            if pygame.sprite.collide_mask(self, box):
                self.rect.x = old_x
                self.rect.y = old_y
                return

    def on_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        step = 10
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            if event.key == pygame.K_LEFT:
                self.move(self.rect.x - step, self.rect.y)
            if event.key == pygame.K_RIGHT:
                self.move(self.rect.x + step, self.rect.y)
            if event.key == pygame.K_UP:
                self.move(self.rect.x, self.rect.y - step)
            if event.key == pygame.K_DOWN:
                self.move(self.rect.x, self.rect.y + step)

    def render(self, surf: Surface) -> None:
        surf.blit(self.sprite, (self.rect.x, self.rect.y))


hero = Hero(20, 390)
industrial_zone = TiledMap('../ind_zone/ind_zone.tmx')
rules = Rules()
start_page = StartPage()
confirmation_dialog = ConfirmationDialog()

while running:
    time_delta = clock.tick(FPS) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            confirmation_dialog.open_confirmation_dialog()

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            running = False
        hero.on_event(event)

        # if event.type == pygame.KEYUP:
        #
        #     if event.key == pygame.K_LEFT:
        #         if shift_of_map < -0.1:
        #             shift_of_map += 0.1
        #             hero.move -= 0.5
        #     if event.key == pygame.K_RIGHT:
        #         if shift_of_map > -35.5:
        #             shift_of_map -= 0.1
        #             hero.move += 0.5
        #         else:
        #             hero.move += 1
        manager.process_events(event)
    manager.update(time_delta)

    if start_page.start_btn.check_pressed():
        mode = 'start'

    elif start_page.rule_btn.check_pressed():
        mode = 'rules'

    elif industrial_zone.pause_btn.check_pressed():
        mode = 'pause'

    elif industrial_zone.cansel.check_pressed():
        mode = 'start'

    elif industrial_zone.back_to_menu.check_pressed():
        mode = 'main'

    elif rules.back_btn.check_pressed():
        mode = 'main'

    start_page.render_back(screen)

    if mode == 'main':
        start_page.render_front(screen)

    elif mode == 'rules':
        rules.render(screen)

    elif mode == 'start':
        industrial_zone.render(screen, shift_of_map)
        hero.render(screen)

    elif mode == 'pause':
        industrial_zone.render(screen, shift_of_map)
        hero.render(screen)
        industrial_zone.open_pause(screen)

    manager.draw_ui(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()