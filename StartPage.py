import pygame.image

from settings import *


class StartPage:
    def __init__(self) -> None:

        self.sound_of_music = 0
        self.sound_of_effects = 0

        self.backgrounds_lst = []
        self.position = 0
        self.last_im = None

        self.x1 = 440
        self.x2 = 440
        self.x3 = 440

        self.backgrounds = (os.listdir(f'{os.path.abspath("BackGrounds")}'))
        self.back_of_settings = pygame.image.load('data/settings.png')

        for i in self.backgrounds:
            self.backgrounds_lst.append(pygame.image.load(f'BackGrounds/{i}'))

        self.image = self.backgrounds_lst[random.randrange(0,
                                                           len(self.backgrounds_lst))]

        self.choose_level = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=['Industrial Zone 1', 'Industrial Zone 2'],
            starting_option='Industrial Zone 1',
            relative_rect=pygame.Rect(255, 275, 165, 50),
            manager=manager)

        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((460, 275), (150, 60)),
                                                      text='Start',
                                                      tool_tip_text='Старт уровня игры',
                                                      manager=manager)

        self.rule_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 275), (150, 50)),
                                                     text='Rules',
                                                     tool_tip_text='Правилила игры',
                                                     manager=manager)

        self.settings_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((820, 20), (150, 50)),
                                                         text='Settings',
                                                         tool_tip_text='Настройки',
                                                         manager=manager)

        self.minus1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 250), (40, 40)),
                                                   text='-',
                                                   manager=manager)
        self.minus1.hide()
        self.plus1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 250), (40, 40)),
                                                  text='+',
                                                  manager=manager)
        self.plus1.hide()

        self.minus2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 375), (40, 40)),
                                                   text='-',
                                                   manager=manager)
        self.minus2.hide()
        self.plus2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 375), (40, 40)),
                                                  text='+',
                                                  manager=manager)
        self.plus2.hide()

        self.minus3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 495), (40, 40)),
                                                   text='-',
                                                   manager=manager)
        self.minus3.hide()
        self.plus3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 495), (40, 40)),
                                                  text='+',
                                                  manager=manager)
        self.plus3.hide()

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
                         (458, 273, 155, 65), 10, 10)

        pygame.draw.rect(surf, 'grey', (658, 273, 155, 55), 10, 10)
        pygame.draw.rect(surf, 'grey', (253, 273, 170, 55), 10, 10)
        pygame.draw.rect(surf, 'grey', (815, 18, 160, 55), 10, 10)

        pict2 = pygame.image.load('data/start_page.png')
        graf2 = pict2.get_rect(bottomright=(1000, 640))
        surf.blit(pict2, graf2)

        self.start_btn.show()
        self.rule_btn.show()
        self.choose_level.show()

    def render_settings(self) -> None:
        screen.blit(self.back_of_settings, (0, 0))

        pygame.draw.rect(screen, 'grey', (815, 18, 160, 55), 10, 10)
        pygame.draw.rect(screen, 'grey', (self.x1, 250, 20, 40))
        pygame.draw.rect(screen, 'grey', (self.x2, 375, 20, 40))
        pygame.draw.rect(screen, 'grey', (self.x3, 495, 20, 40))

        if self.minus1.check_pressed() and self.x1 > 440:
            self.x1 -= 10
            self.sound_of_music -= 0.02272727
            self.sound_of_effects -= 0.02272727

            pygame.mixer.music.set_volume(self.sound_of_music)
            btn_sound.set_volume(self.sound_of_effects)
            win_sound.set_volume(self.sound_of_effects)
            shoot_sound.set_volume(self.sound_of_effects)

        if self.plus1.check_pressed() and self.x1 < 880:
            self.x1 += 10
            self.sound_of_music += 0.02272727
            self.sound_of_effects += 0.02272727

            pygame.mixer.music.set_volume(self.sound_of_music)
            btn_sound.set_volume(self.sound_of_effects)
            win_sound.set_volume(self.sound_of_effects)
            shoot_sound.set_volume(self.sound_of_effects)

        if self.minus2.check_pressed() and self.x2 > 440:
            self.x2 -= 10
            self.sound_of_music -= 0.02272727

            pygame.mixer.music.set_volume(self.sound_of_music)

        if self.plus2.check_pressed() and self.x2 < 880:
            self.x2 += 10
            self.sound_of_music += 0.02272727

            pygame.mixer.music.set_volume(self.sound_of_music)

        if self.minus3.check_pressed() and self.x3 > 440:
            self.x3 -= 10
            self.sound_of_effects -= 0.02272727

            btn_sound.set_volume(self.sound_of_effects)
            win_sound.set_volume(self.sound_of_effects)
            shoot_sound.set_volume(self.sound_of_effects)

        if self.plus3.check_pressed() and self.x3 < 880:
            self.x3 += 10
            self.sound_of_effects += 0.02272727

            btn_sound.set_volume(self.sound_of_effects)
            win_sound.set_volume(self.sound_of_effects)
            shoot_sound.set_volume(self.sound_of_effects)
