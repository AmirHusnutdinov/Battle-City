from settings import *
from StartPage import StartPage
from confirmation_dialog import ConfirmationDialog
from rules import Rules
from Map import TiledMap, AnimatedThings
from Hero import Hero
from Win_or__Lose import WinOrLose


mode = 'main'
running = True
win_or_lose = WinOrLose(screen, mode)
hero = Hero(200, 200)
level_map = []
with open('ind_zone/floor.txt', mode='r') as file:
    level_map.append([line.strip() for line in file])
with open('ind_zone/wall.txt', mode='r') as file:
    level_map.append([line.strip() for line in file])
with open('ind_zone/decor.txt', mode='r') as file:
    level_map.append([line.strip() for line in file])
industrial_zone = TiledMap(level_map)
rules = Rules()
start_page = StartPage()
confirmation_dialog = ConfirmationDialog()
press1, press2 = AnimatedThings(322, 417, 4), AnimatedThings(417, 417, 4)
scan1, scan2, scan3, scan4 = AnimatedThings(130, 419, 1), AnimatedThings(898, 386, 1), \
    AnimatedThings(1794, 353, 1), AnimatedThings(2179, 321, 1)
screen1 = AnimatedThings(641, 450, 2)
conveer1, conveer2, conveer3 = AnimatedThings(225, 481, 3), AnimatedThings(323, 481, 3), AnimatedThings(418, 481, 3)

while running:
    time_delta = clock.tick(FPS) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            confirmation_dialog.open_confirmation_dialog()

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            btn_sound.play()
            running = False
        hero.on_event(event)

        manager.process_events(event)
    manager.update(time_delta)

    if start_page.start_btn.check_pressed() or \
            industrial_zone.cansel.check_pressed() or win_or_lose.restart.check_pressed():
        mode = 'start'
        pygame.mixer.music.unpause()
        win_or_lose.x = 0
        win_or_lose.y = -600
        win_or_lose.y1 = win_or_lose.y2 = 700
        win_or_lose.restart.hide()
        win_or_lose.menu.hide()

        btn_sound.play()

        industrial_zone.cansel.hide()
        industrial_zone.pause_btn.hide()
        industrial_zone.back_to_menu.hide()
        industrial_zone.pause_btn.show()

        start_page.rule_btn.hide()
        start_page.choose_level.hide()
        start_page.start_btn.hide()

    elif start_page.rule_btn.check_pressed():
        mode = 'rules'
        btn_sound.play()
        
        start_page.start_btn.hide()
        start_page.rule_btn.hide()
        start_page.choose_level.hide()

    elif industrial_zone.pause_btn.check_pressed():
        pygame.mixer.music.pause()
        mode = 'pause'
        btn_sound.play()

    elif industrial_zone.back_to_menu.check_pressed() or \
            rules.back_btn.check_pressed() or win_or_lose.menu.check_pressed():
        mode = 'main'
        pygame.mixer.music.unpause()
        win_or_lose.restart.hide()
        win_or_lose.menu.hide()
        rules.back_btn.hide()
        btn_sound.play()

    elif industrial_zone.death.check_pressed():
        mode = 'death'
        pygame.mixer.music.pause()
        lose.play()
        btn_sound.play()

    elif industrial_zone.win.check_pressed():
        pygame.mixer.music.pause()
        mode = 'win'
        industrial_zone.pause_btn.hide()
        win.play()
        btn_sound.play()

    start_page.render_back(screen)

    if mode == 'main':
        start_page.render_front(screen)
        industrial_zone.cansel.hide()
        industrial_zone.pause_btn.hide()
        industrial_zone.back_to_menu.hide()

    elif mode == 'rules':
        rules.render(screen)

    elif mode == 'start':
        industrial_zone.render(screen)
        industrial_zone.update()
        press1.render()
        press2.render()
        scan1.render()
        scan2.render()
        scan3.render()
        scan4.render()
        screen1.render()
        conveer1.render()
        conveer2.render()
        conveer3.render()

    elif mode == 'pause':
        industrial_zone.render(screen)
        industrial_zone.update()
        industrial_zone.open_pause(screen)

    elif mode == 'death' or mode == 'win':
        industrial_zone.render(screen)
        industrial_zone.pause_btn.hide()
        win_or_lose.render(mode)
    manager.draw_ui(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
