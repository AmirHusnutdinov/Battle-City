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
        self.backgrounds = (os.listdir(f'{os.path.abspath("BackGrounds")}'))

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

        self.graffiti = (os.listdir(f'{os.path.abspath("graffiti")}'))
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
        
        pict2 = pygame.image.load('rules.png')
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
        # Удали эту кнопку как появится смерть
        self.death = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100, 140, 40)),
                                                   text='Смэрть',
                                                   manager=manager)

        self.pause = pygame.image.load('pause.png')

        self.pause_btn.hide()
        self.back_to_menu.hide()
        self.cansel.hide()

    def render(self, surf: Surface, shift: float) -> None:
        image = pygame.image.load('ind_zone/Background_new.png')
        
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
        pygame.draw.rect(surf, 'black', (403, 299, 144, 43), 10,  4)
        pygame.draw.rect(surf, 'black', (553, 299, 144, 43), 10, 4)


class Hero:
    def __init__(self) -> None:
        self.sprite = pygame.image.load('Hero/p1.png')
        self.is_move = False
        self.direction = 'right'
        self.move = 20

    def render(self, surf: Surface) -> None:
        surf.blit(self.sprite, (self.move, 390))


class GameOver:
    def __init__(self):
        self.image = pygame.image.load('game_over.png')
        self.menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((329, 328, 150, 60)),
                                                   text='Главное меню',
                                                   manager=manager)
        self.restart = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((610, 328, 150, 60)),
                                                   text='Начать с начала',
                                                   manager=manager)
        self.menu.hide()
        self.restart.hide()
        self.x = 0
        self.y = -600
        self.y1 = self.y2 = 700

    def render(self, surf: Surface):
        industrial_zone.pause_btn.hide()
        surf.blit(self.image, (self.x, self.y))
        color = (255, random.randrange(1, 256), random.randrange(1, 256))
        pygame.draw.rect(surf, color, (327, self.y1, 155, 66), 10, 10)
        pygame.draw.rect(surf, color, (608, self.y2, 155, 66), 10, 10)
        if self.y < 0:
            self.y += FPS
        if self.y1 > 339:
            self.y1 -= FPS // 2
            self.menu.show()
        if self.y2 > 339:
            self.y2 -= FPS // 2
            self.restart.show()


game_over = GameOver()
hero = Hero()
industrial_zone = TiledMap('ind_zone/ind_zone.tmx')
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

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                if shift_of_map < -0.1:
                    shift_of_map += 0.1
                    hero.move -= 0.5
            if event.key == pygame.K_RIGHT:
                if shift_of_map > -35.5:
                    shift_of_map -= 0.1
                    hero.move += 0.5
                else:
                    hero.move += 1
        manager.process_events(event)
    manager.update(time_delta)

    if start_page.start_btn.check_pressed() or\
            industrial_zone.cansel.check_pressed() or game_over.restart.check_pressed():
        mode = 'start'
        game_over.x = 0
        game_over.y = -600
        game_over.y1 = game_over.y2 = 700
        game_over.restart.hide()
        game_over.menu.hide()

    elif start_page.rule_btn.check_pressed():
        mode = 'rules'

    elif industrial_zone.pause_btn.check_pressed():
        mode = 'pause'

    elif industrial_zone.back_to_menu.check_pressed() or\
            rules.back_btn.check_pressed() or game_over.menu.check_pressed():
        mode = 'main'
        game_over.restart.hide()
        game_over.menu.hide()

    elif industrial_zone.death.check_pressed():
        mode = 'death'

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

    elif mode == 'death':
        industrial_zone.render(screen, shift_of_map)
        hero.render(screen)
        game_over.render(screen)

    manager.draw_ui(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
