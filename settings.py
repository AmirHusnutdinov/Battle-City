import os
import random

import pygame
import pygame_gui
import pytmx
from pygame import Surface

running = True

FPS = 50
shift_of_map = 0

pygame.init()
pygame.display.set_caption('Great way')
size = (1100, 600)
screen = pygame.display.set_mode(size)

manager = pygame_gui.UIManager((1100, 600))
clock = pygame.time.Clock()
pygame.mixer.music.load('music/m.mp3')
pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.1)
lose = pygame.mixer.Sound('music/lose.mp3')
lose.set_volume(0.2)

btn_sound = pygame.mixer.Sound('music/btn.mp3')
win = pygame.mixer.Sound('music/win.mp3')
win.set_volume(0.3)