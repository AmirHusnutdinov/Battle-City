from Sprites import Walls
from settings import *

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

dict_walls = {
    'y': '03',
    'u': '11',
    'i': '26',
    'o': '12',
    'p': '02',
    'g': '21',
    'h': '46',
    '&': '45',
    '^': '54',
    '~': '63',
    '/': '61',
    '+': '70',
    'l': 'Pointer1',
    '[': 'Fence1',
    ']': 'Fence2',
    '=': 'Fence3',
    'й': '10',
    'ц': '01',
    'у': '19',
    'г': '39',
    'я': '29',
    'ч': '20',
    'ф': '30'
}

dict_decor = {
    'd': 'Locker1',
    'a': 'Fire-extinguisher2',
    'f': 'Locker4',
    'z': 'Mop',
    'x': 'Bucket',
    'c': 'Board3',
    'v': 'Box4',
    'b': 'Box3',
    'n': 'Box5',
    'm': 'Bench',
    '}': 'Box1',
    '{': 'Box2',
    '-': 'Barrel4',
    '_': 'Barrel3'
}


class TiledMap:

    def __init__(self, filename: list) -> None:

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
        self.floor_layer = filename[0]
        self.wall_layer = filename[1]
        self.decor_layer = filename[2]
        self.cells = pygame.sprite.Group()
        self.decor_cells = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()

    def render(self, surf: Surface) -> None:
        image = pygame.image.load('ind_zone/Backgroundnew.png')
        surf.blit(image, (0, 0))
        surf.blit(image, (1067, 0))

        rows = len(self.floor_layer)
        for i in range(rows):
            for ix, value in enumerate(self.floor_layer[i]):
                if value in dict_floor.keys():
                    floor = Walls(ix * SPRITE, i * SPRITE, f'IndustrialTile_{dict_floor[value]}.png')
                    self.boxes.add(floor)
        rows = len(self.wall_layer)
        for i in range(rows):
            for ix, value in enumerate(self.wall_layer[i]):
                if value in dict_walls.keys():
                    if len(dict_walls[value]) < 3:
                        wall = Walls(ix * SPRITE, i * SPRITE, f'IndustrialTile_{dict_walls[value]}.png')
                    else:
                        wall = Walls(ix * SPRITE, i * SPRITE, f'{dict_walls[value]}.png')
                    self.cells.add(wall)
        rows = len(self.decor_layer)
        for i in range(rows):
            for ix, value in enumerate(self.decor_layer[i]):
                if value in dict_decor.keys():
                    wall = Walls(ix * SPRITE, i * SPRITE, f'{dict_decor[value]}.png')
                    self.decor_cells.add(wall)

        self.back_to_menu.hide()
        self.cansel.hide()
        pygame.draw.rect(surf, 'black', (978, 18, 104, 54), 4, 10)

    def update(self) -> None:
        self.cells.draw(screen)
        self.decor_cells.draw(screen)
        self.boxes.draw(screen)

    def open_pause(self, surf: Surface) -> None:
        self.back_to_menu.show()
        self.cansel.show()
        surf.blit(self.pause, (400, 200))
        pygame.draw.rect(surf, 'black', (397, 197, 307, 206), 4, 10)
        pygame.draw.rect(surf, 'black', (403, 299, 144, 43), 10, 4)
        pygame.draw.rect(surf, 'black', (553, 299, 144, 43), 10, 4)


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
