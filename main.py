import os
import random

import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption('start')
size = (1100, 600)
screen = pygame.display.set_mode(size)

manager = pygame_gui.UIManager((1100, 600))

mass = []
backgrounds = (os.listdir(f'{os.path.abspath("BackGrounds")}'))
for i in backgrounds:
    mass.append(pygame.image.load(f'BackGrounds/{i}'))
image = mass[random.randrange(0, len(mass))]

choose_level = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
                                    options_list=['Industrial Zone', 'Castle Zone', 'Green Zone'],
                                    starting_option='Industrial Zone',
                                    relative_rect=pygame.Rect(300, 275, 150, 50),
                                    manager=manager,)

start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (150, 60)),
                                    text='Start',
                                    tool_tip_text='Нажми ты уже эту кнопку!',
                                    manager=manager)

rule_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 275), (150, 50)),
                                    text='Rules',
                                    tool_tip_text='Нажми ты уже эту кнопку!',
                                    manager=manager)

back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((930, 20), (150, 50)),
                                    text='Come back',
                                    tool_tip_text='Нажми ты уже эту кнопку!',
                                    manager=manager)

clock = pygame.time.Clock()
running = True
position = 0
v = 40
mode = 'main'

while running:
    time_delta = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            confirmation_dialog1 = pygame_gui.windows.UIConfirmationDialog(
                rect=pygame.Rect((400, 100), (300, 200)),
                manager=manager,
                window_title='Подтверждение',
                action_long_desc='Вы уверены, что хотите выйти ?',
                action_short_name='YES',
                blocking=True)

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            running = False

        manager.process_events(event)
    manager.update(time_delta)
    
    if start_btn.check_pressed():
        pass

    elif rule_btn.check_pressed():
        mode = 'rules'

    screen.blit(image, (position, 0))
    if position > - 100:
        position -= v * clock.tick(60) / 1000
    else:
        last_im = image
        image = mass[random.randrange(0, len(mass))]
        while image == last_im:
            image = mass[random.randrange(0, len(mass))]
        position = random.randrange(-5, 2)

    if mode == 'main':
        back_btn.hide()
        im2 = pygame.image.load('img/Name.png')
        logo = im2.get_rect(
            bottomright=(700, 250))
        screen.blit(im2, logo)

        im3 = pygame.image.load('img/Choose_level.png')
        logo2 = im3.get_rect(
            bottomright=(300, 440))
        screen.blit(im3, logo2)

        graffiti = (os.listdir(f'{os.path.abspath("graffiti")}'))
        coords = [(300, 500), (700, 500), (150, 400),
                  (500, 450), (900, 100), (300, 150),
                  (960, 300), (600, 100), (980, 500)]
        for i in range(len(graffiti)):
            pict = pygame.image.load(f'graffiti/{graffiti[i]}')
            graf = pict.get_rect(bottomright=(coords[i]))
            screen.blit(pict, graf)

    elif mode == 'rules':
        back_btn.show()
        start_btn.hide()
        rule_btn.hide()
        choose_level.hide()
        if back_btn.check_pressed():
            mode = 'main'
            start_btn.show()
            rule_btn.show()
            choose_level.show()

        pict2 = pygame.image.load('rules.png')
        graf2 = pict2.get_rect(bottomright=(1100, 600))
        screen.blit(pict2, graf2)

    manager.draw_ui(screen)
    pygame.display.flip()
quit()
