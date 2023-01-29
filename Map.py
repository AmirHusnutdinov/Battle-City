from Box2D import b2PolygonShape, b2CircleShape
from pygame import Color

from Walls import Walls
from settings import *
from Hero import Hero
PPM = 20.0

dict_floor = {
    '1': '73',
    '2': '04',
    '3': '13',
    '4': '05',
    '5': '06',
    '6': '15',
    '7': '16',
    '8': '14',
    '9': '67',
    'q': '22',
    'w': '24',
    'j': '71',
    'k': '36',
    '<': '27',
    '>': '62',
    ';': '81',
    '!': '31',
    '?': '40',
    '%': '49',
    '#': '50',
    '$': '51',
    '@': '42',
    '(': '33',
    ')': '32',
    '*': '41',
    '&': '45',
    '^': '54',
    '~': '63',
    '/': '61',
    '+': '70',
    'ы': '23',
    'э': '17',
    'з': '72',
    'в': '80'

}

class TiledMap:

    def __init__(self, filename: str) -> None:

        self.pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 20, 100, 50)),
                                                      text='Pause',
                                                      manager=manager)
        self.back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((405, 300, 140, 40)),
                                                         text='Главное меню',
                                                         manager=manager)
        self.cansel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((555, 300, 140, 40)),
                                                   text='Отмена',
                                                   manager=manager)
        # Удали эти кнопкb как появится смерть
        self.death = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0, 40, 40)),
                                                  text='Смэрть',
                                                  manager=manager)
        self.win = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 0, 40, 40)),
                                                text='win',
                                                manager=manager)

        self.pause = pygame.image.load('data/pause.png')

        self.pause_btn.hide()
        self.back_to_menu.hide()
        self.cansel.hide()
        self.all_sprites = pygame.sprite.Group()
        self.data = filename
        self.boxes = pygame.sprite.Group()

    def render(self, surf: Surface) -> None:
        rows = len(self.data)
        for i in range(rows):
            for ix, value in enumerate(self.data[i]):
                if value in dict_floor.keys():
                    wall = Walls(ix * SPRITE, i * SPRITE, f'IndustrialTile_{dict_floor[value]}.png')
                    self.boxes.add(wall)

        self.back_to_menu.hide()
        self.cansel.hide()
        pygame.draw.rect(surf, 'black', (978, 18, 104, 54), 4, 10)

    def update(self):
        self.boxes.draw(screen)

    def open_pause(self, surf: Surface) -> None:
        self.back_to_menu.show()
        self.cansel.show()
        surf.blit(self.pause, (400, 200))

        pygame.draw.rect(surf, 'black', (397, 197, 307, 206), 4, 10)
        pygame.draw.rect(surf, 'black', (403, 299, 144, 43), 10, 4)
        pygame.draw.rect(surf, 'black', (553, 299, 144, 43), 10, 4)
