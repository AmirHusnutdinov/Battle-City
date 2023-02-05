import os
import sys
import random
import pygame
import pygame_gui
from pygame import Surface

running = True
SPRITE = 32
FPS = 50
shift_of_map = 0

pygame.init()
pygame.display.set_caption('Great way')
size = WIDTH, HEIGHT = (992, 640)
screen = pygame.display.set_mode(size)

manager = pygame_gui.UIManager((1100, 640))
clock = pygame.time.Clock()

pygame.mixer.music.load('./music/start.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

btn_sound = pygame.mixer.Sound('music/btn.mp3')
btn_sound.set_volume(0)

win_sound = pygame.mixer.Sound('music/win.mp3')
win_sound.set_volume(0)

shoot_sound = pygame.mixer.Sound('music/shoot.mp3')
shoot_sound.set_volume(0)


def load_image(name):
    fullname = os.path.join('sprites_map', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображениями "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Sprite(pygame.sprite.Sprite):
    sprite = None

    def __init__(self, x: int, y: int, sprite=None) -> None:
        super().__init__()
        if sprite is not None:
            self.image = load_image(sprite)
        else:
            self.image = self.__class__.sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.rect.width < SPRITE:
            self.rect.x += (SPRITE - self.rect.width) // 2
        if self.rect.height < SPRITE:
            self.rect.y += (SPRITE - self.rect.height) // 2
        self.mask = pygame.mask.from_surface(self.image)

    def on_event(self, event):
        pass
