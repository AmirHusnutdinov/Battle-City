import os
import random

import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption('start')
size = (1100, 600)
screen = pygame.display.set_mode(size)

manager = pygame_gui.UIManager((1100, 600))
clock = pygame.time.Clock()
running = True
mode = 'main'


class StartPage:
    def __init__(self):
        self.mass = []
        self.position = 0
        self.v = 40
        self.last_im = None
        self.graffiti = None
        self.coordinates = []
        self.pict = None
        self.graf = None
        self.backgrounds = (os.listdir(f'{os.path.abspath("BackGrounds")}'))

        for i in self.backgrounds:
            self.mass.append(pygame.image.load(f'BackGrounds/{i}'))
        self.image = self.mass[random.randrange(0, len(self.mass))]

        self.choose_level = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=['Industrial Zone', 'Green Zone'],
            starting_option='Industrial Zone',
            relative_rect=pygame.Rect(300, 275, 150, 50),
            manager=manager, )

        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (150, 60)),
                                                      text='Start',
                                                      tool_tip_text='Press this Button!',
                                                      manager=manager)

        self.rule_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 275), (150, 50)),
                                                     text='Rules',
                                                     tool_tip_text='Press this Button!',
                                                     manager=manager)

    def render_back(self):
        screen.blit(self.image, (self.position, 0))
        if self.position > - 100:
            self.position -= self.v * clock.tick(60) / 1000
        else:
            self.last_im = self.image
            self.image = self.mass[random.randrange(0, len(self.mass))]
            while self.image == self.last_im:
                self.image = self.mass[random.randrange(0, len(self.mass))]
            self.position = random.randrange(-5, 2)

    def render_front(self):
        rules.back_btn.hide()
        self.graffiti = (os.listdir(f'{os.path.abspath("graffiti")}'))
        self.coordinates = [(300, 500), (700, 500), (150, 400),
                            (500, 450), (900, 100), (300, 150),
                            (960, 300), (600, 100), (980, 500),
                            (300, 440), (700, 250)]
        for i in range(len(self.graffiti)):
            self.pict = pygame.image.load(f'graffiti/{self.graffiti[i]}')
            self.graf = self.pict.get_rect(bottomright=(self.coordinates[i]))
            screen.blit(self.pict, self.graf)


class ConfirmationDialog:
    def __init__(self):
        self.confirmation_dialog1 = None

    def open_confirmation_dialog(self):
        self.confirmation_dialog1 = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect((400, 100), (300, 200)),
            manager=manager,
            window_title='Confirm',
            action_long_desc='Вы уверены, что хотите выйти ?',
            action_short_name='YES',
            blocking=True)


class Rules:
    def __init__(self):
        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((930, 20), (150, 50)),
                                                     text='Come back',
                                                     tool_tip_text='Press this Button!',
                                                     manager=manager)

    def render(self):
        self.back_btn.show()
        start_page.start_btn.hide()
        start_page.rule_btn.hide()
        start_page.choose_level.hide()
        pict2 = pygame.image.load('rules.png')
        graf2 = pict2.get_rect(bottomright=(1100, 600))
        screen.blit(pict2, graf2)

    def press_event(self):
        if self.back_btn.check_pressed():
            global mode
            mode = 'main'
            start_page.start_btn.show()
            start_page.rule_btn.show()
            start_page.choose_level.show()


rules = Rules()
start_page = StartPage()
confirmation_dialog = ConfirmationDialog()

while running:
    time_delta = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            confirmation_dialog.open_confirmation_dialog()

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            running = False

        manager.process_events(event)
    manager.update(time_delta)

    if start_page.start_btn.check_pressed():
        pass

    elif start_page.rule_btn.check_pressed():
        mode = 'rules'

    start_page.render_back()

    if mode == 'main':
        start_page.render_front()

    elif mode == 'rules':
        rules.render()
        if rules.back_btn.check_pressed():
            rules.press_event()

    manager.draw_ui(screen)
    pygame.display.flip()
pygame.quit()
