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
backgrounds = (os.listdir(f'{os.path.abspath("data")}'))
for i in backgrounds:
    mass.append(pygame.image.load(f'data/{i}'))
image = mass[random.randrange(0, len(mass))]
l1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(450, 100, 200, 100),
                                 text='Mega Game',

                                 manager=manager)
l1.set_text_scale(scale=2)
choose_level = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
                                    options_list=['Industrial Zone', 'Castle Zone', 'Green Zone'],
                                    starting_option='Industrial Zone',
                                    relative_rect=pygame.Rect(300, 275, 150, 50),
                                    manager=manager,)

l2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(100, 200, 200, 100),
                                 text='Choose level',
                                 manager=manager)


btn2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (150, 60)),
                                    text='Start',
                                    tool_tip_text='Нажми ты уже эту кнопку!!!',
                                    manager=manager)
btn3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 275), (150, 50)),
                                    text='Правила',
                                    tool_tip_text='Нажми ты уже эту кнопку!!!',
                                    manager=manager)

clock = pygame.time.Clock()
running = True
count = 0
v = 40

while running:
    time_delta = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
                rect=pygame.Rect((400, 100), (300, 200)),
                manager=manager,
                window_title='Подтверждение',
                action_long_desc='Вы уверены, что хотите выйти ?',
                action_short_name='YES',
                blocking=True
            )
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                running = False
        manager.process_events(event)
    manager.update(time_delta)
    screen.blit(image, (count, 0))
    pygame.draw.line(screen, 'white', (250, 250), (300, 300), 4)
    pygame.draw.line(screen, 'white', (300, 300), (300, 280), 3)
    pygame.draw.line(screen, 'white', (300, 300), (280, 300), 3)
    if count > - 100:
        count -= v * clock.tick(60) / 1000
    else:
        last_im = image
        image = mass[random.randrange(0, len(mass))]
        while image == last_im:
            image = mass[random.randrange(0, len(mass))]
        count = random.randrange(-5, 2)
    if btn2.check_pressed():
        print(1)
    elif btn3.check_pressed():
        print(2)
    manager.draw_ui(screen)
    l1.set_text_scale(scale=3)
    pygame.display.flip()
quit()
