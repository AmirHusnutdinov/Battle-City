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
mass = []
heroes = (os.listdir(f'{os.path.abspath("hero/hero_stay/normal")}'))
print(heroes)
for i in range(len(heroes)):
    pict = pygame.image.load(f'hero/hero_stay/normal/{heroes[i]}')
    mass.append(pict)
count = 0

mass2 = []
heroes2 = (os.listdir(f'{os.path.abspath("hero/hero_ran/normal")}'))
for i in range(len(heroes2)):
    pict2 = pygame.image.load(f'hero/hero_ran/normal/{heroes2[i]}')
    mass2.append(pict2)
count2 = 0

mass3 = []
heroes3 = (os.listdir(f'{os.path.abspath("hero/hero_jump/normal")}'))
for i in range(len(heroes3)):
    pict3 = pygame.image.load(f'hero/hero_jump/normal/{heroes3[i]}')
    mass3.append(pict3)
count3 = 0

mass4 = []
heroes4 = (os.listdir(f'{os.path.abspath("hero/hero_attack/normal")}'))
for i in range(len(heroes4)):
    pict4 = pygame.image.load(f'hero/hero_attack/normal/{heroes4[i]}')
    mass4.append(pict4)
count4 = 0

mass5 = []
heroes5 = (os.listdir(f'{os.path.abspath("hero/hero_death/normal")}'))
for i in range(len(heroes5)):
    pict5 = pygame.image.load(f'hero/hero_death/normal/{heroes5[i]}')
    mass5.append(pict5)
count5 = 0

mass6 = []
heroes6 = (os.listdir(f'{os.path.abspath("hero/hero_climb")}'))
for i in range(len(heroes6)):
    pict6 = pygame.image.load(f'hero/hero_climb/{heroes6[i]}')
    mass6.append(pict6)
count6 = 0

mass7 = []
heroes7 = (os.listdir(f'{os.path.abspath("hero/hero_run_attack/normal")}'))
for i in range(len(heroes7)):
    pict7 = pygame.image.load(f'hero/hero_run_attack/normal/{heroes7[i]}')
    mass7.append(pict7)
count7 = 0
a = AnimatedThings(200, 100, 4)

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
        # hero.all_sprites.draw(screen
        if count < 3 or count3 < 3:
            count += 1
            count3 += 1
        else:
            count = 0
            count3 = 0

        if count2 < 5 or count6 < 5 or count7 < 5:
            count2 += 1
            count6 += 1
            count7 += 1
        else:
            count2 = 0
            count6 = 0
            count7 = 0

        if count4 < 13:
            count4 += 1
        else:
            count4 = 0

        if count5 < 7:
            count5 += 1
        else:
            count5 = 0

        screen.blit(mass[count], (200, 200))
        screen.blit(mass2[count2], (300, 200))
        screen.blit(mass3[count3], (400, 200))
        screen.blit(mass4[count4], (500, 200))
        screen.blit(mass5[count5], (600, 200))
        screen.blit(mass6[count6], (700, 200))
        screen.blit(mass7[count7], (800, 200))
        a.render()

        #hero.render(screen)

    elif mode == 'pause':
        industrial_zone.render(screen)
        #hero.render(screen)
        industrial_zone.open_pause(screen)

    elif mode == 'death' or mode == 'win':
        industrial_zone.render(screen)
        industrial_zone.pause_btn.hide()
        #hero.render(screen)
        win_or_lose.render(mode)
    manager.draw_ui(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
