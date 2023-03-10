from settings import *
from StartPage import StartPage
from confirmation_dialog import ConfirmationDialog
from rules import Rules
from Map import Map
from Win_or__Lose import WinOrLose

mode = 'main'
running = True

with open(f'sprites_map/map1.txt', mode='r') as file:
    level_map1 = [line.strip() for line in file]

industrial_zone = Map(level_map1)
win_or_lose = WinOrLose(screen, mode)
rules = Rules()
start_page = StartPage()
confirmation_dialog = ConfirmationDialog()


def hide_start_page_btn() -> None:
    start_page.settings_btn.hide()
    start_page.start_btn.hide()
    start_page.rule_btn.hide()
    start_page.choose_level.hide()


while running:

    time_delta = clock.tick(FPS) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            confirmation_dialog.open_confirmation_dialog()

        if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
            btn_sound.play()
            with open('music/sound_level.txt', 'w') as f2:
                f2.write(f'{str(start_page.sound_of_music)}\n')
                f2.write(f'{str(start_page.sound_of_effects)}\n')
                f2.write(f'{str(start_page.x1)}\n')
                f2.write(f'{str(start_page.x2)}\n')
                f2.write(f'{str(start_page.x3)}\n')

            running = False

        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:

            if event.text == 'Industrial Zone 1':
                name_of_map = '1'

            else:
                name_of_map = '2'

            with open(f'sprites_map/map{name_of_map}.txt', mode='r') as file:
                level_map1 = [line.strip() for line in file]
                industrial_zone = Map(level_map1)

        industrial_zone.on_event(event, mode)
        manager.process_events(event)

    manager.update(time_delta)
    industrial_zone.update()
    from Map import kill_info

    if start_page.start_btn.check_pressed() or \
            industrial_zone.cansel.check_pressed() or\
            win_or_lose.restart.check_pressed():

        mode = 'start'
        kill_info = None

        pygame.mixer.music.load('./music/motor.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(start_page.sound_of_effects)
        pygame.mixer.music.unpause()
        btn_sound.play()

        win_or_lose.x = 0
        win_or_lose.y = -600
        win_or_lose.y1 = win_or_lose.y2 = 700
        win_or_lose.restart.hide()
        win_or_lose.menu.hide()

        start_page.settings_btn.hide()

        if start_page.start_btn.check_pressed() \
                or win_or_lose.restart.check_pressed():
            industrial_zone = Map(level_map1)
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
        hide_start_page_btn()

    elif start_page.settings_btn.check_pressed():
        mode = 'settings'
        hide_start_page_btn()

        start_page.minus1.show()
        start_page.plus1.show()
        start_page.minus2.show()
        start_page.plus2.show()
        start_page.minus3.show()
        start_page.plus3.show()

        btn_sound.play()
        rules.back_btn.show()

    elif industrial_zone.pause_btn.check_pressed():
        pygame.mixer.music.pause()
        mode = 'pause'
        btn_sound.play()

    elif industrial_zone.back_to_menu.check_pressed() or \
            rules.back_btn.check_pressed() or win_or_lose.menu.check_pressed():
        mode = 'main'
        kill_info = None

        pygame.mixer.music.load('./music/start.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(start_page.sound_of_music)
        pygame.mixer.music.unpause()
        btn_sound.play()

        win_or_lose.restart.hide()
        win_or_lose.menu.hide()

        rules.back_btn.hide()

        start_page.minus1.hide()
        start_page.plus1.hide()
        start_page.minus2.hide()
        start_page.plus2.hide()
        start_page.minus3.hide()
        start_page.plus3.hide()
        start_page.settings_btn.show()

    if mode != 'main':
        if kill_info == 'green kill':
            mode = 'red win'
            pygame.mixer.music.pause()
            industrial_zone.pause_btn.hide()

        elif kill_info == 'red kill':
            pygame.mixer.music.pause()
            mode = 'green win'
            industrial_zone.pause_btn.hide()

    start_page.render_back(screen)

    if mode == 'main':
        start_page.render_front(screen)

        industrial_zone.cansel.hide()
        industrial_zone.pause_btn.hide()
        industrial_zone.back_to_menu.hide()

    elif mode == 'rules':
        rules.render(screen)

    elif mode == 'start' or mode == 'pause':
        industrial_zone.render(screen)
        industrial_zone.update()
        if mode == 'pause':
            industrial_zone.open_pause(screen)

    elif mode == 'death' or mode == 'win':
        industrial_zone.render(screen)
        industrial_zone.pause_btn.hide()
        win_or_lose.render(mode)

    elif mode == 'settings':
        start_page.render_settings()

    elif mode == 'green win':
        win_or_lose.render(mode)
        win_sound.play()

    elif mode == 'red win':
        win_or_lose.render(mode)
        win_sound.play()

    manager.draw_ui(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
