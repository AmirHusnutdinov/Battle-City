from settings import *


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
            options_list=['Industrial Zone', 'Coming soon...'],
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
