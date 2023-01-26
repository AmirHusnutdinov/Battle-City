import sys

import setuptools.config
from pygame import Surface, Color
import pygame
import os
from typing import Tuple
FPS = 50
SIZE = WIDTH, HEIGHT = 550, 550
SPRITE = 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображениями "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Scene:
    def __init__(self, screen: Surface, to_next_scene=None):
        self.screen = screen
        self.to_next_scene = to_next_scene

    def update(self):
        pass

    def on_event(self, event):
        pass


class StartScreen(Scene):
    def __init__(self, screen: Surface, to_next_scene=None):
        super().__init__(screen, to_next_scene)

    def on_event(self, event):
        if self.to_next_scene is None:
            return

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.to_next_scene()

    def update(self):
        self.screen.fill(Color('black'))
        font = pygame.font.Font(None, 50)
        text = font.render('My game', True, Color('white'))
        rect = text.get_rect()
        rect.x = int(WIDTH // 2 - rect.width // 2)
        rect.y = HEIGHT // 2 - rect.height - 20
        self.screen.blit(text, rect)
        font = pygame.font.Font(None, 30)
        text = font.render('press SPACE to start', True, Color('white'))
        rect = text.get_rect()
        rect.x = int(WIDTH // 2 - rect.width // 2)
        rect.y = HEIGHT // 2 + 10
        self.screen.blit(text, rect)


class Sprite(pygame.sprite.Sprite):
    sprite = None

    def __init__(self, x: int, y: int):
        super().__init__()
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


class Cell(Sprite):
    sprite = load_image('grass.png')


class Box(Sprite):
    sprite = load_image('box.png')


class Hero(Sprite):
    sprite = load_image('mar.png')

    def set_boxes(self, boxes: pygame.sprite.Group):
        self.boxes = boxes

    def move(self, x, y):
        old_x = self.rect.x
        old_y = self.rect.y
        if x < 0 or y < 0:
            return
        if x + self.rect.width > WIDTH or old_y + self.rect.height > HEIGHT:
            return
        self.rect.x = x
        self.rect.y =y
        if not self.boxes:
            return
        for box in self.boxes.sprites():
            if pygame.sprite.collide_mask(self, box):
                self.rect.x = old_x
                self.rect.y = old_y
                return

    def on_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        step = 10
        if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            if event.key == pygame.K_LEFT:
                self.move(self.rect.x - step, self.rect.y)
            if event.key == pygame.K_RIGHT:
                self.move(self.rect.x + step, self.rect.y)
            if event.key == pygame.K_UP:
                self.move(self.rect.x, self.rect.y - step)
            if event.key == pygame.K_DOWN:
                self.move(self.rect.x, self.rect.y + step)


class Level(Scene):
    def __init__(self, screen: Surface, data, to_next_scene=None):
        super().__init__(screen, to_next_scene)
        self.all_sprites = pygame.sprite.Group()
        boxes = pygame.sprite.Group()
        self.hero = None
        rows = len(data)
        cols = max(map(len, data))
        for i in range(rows):
            row = str(data[i]).ljust(cols, '.')
            for ix, value in enumerate(row):
                if value == '.' or value == '@':
                    self.all_sprites.add(Cell(ix * SPRITE, i * SPRITE))
                elif value == '#':
                    box = Box(ix * SPRITE, i * SPRITE)
                    self.all_sprites.add(box)
                    boxes.add(box)
                if value == '@':
                    self.hero = Hero(ix * SPRITE, i * SPRITE)

        if self.hero:
            self.all_sprites.add(self.hero)
            self.hero.set_boxes(boxes)

    def update(self):
        self.screen.fill(Color('white'))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update()

    def on_event(self, event):
        for sprite in self.all_sprites.sprites():
            sprite.on_event(event)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        self.scene = StartScreen(self.screen, self.__go_to_level)

    def start(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                self.scene.on_event(event)
            self.scene.update()
            pygame.display.flip()
            clock.tick(FPS)

    def __go_to_level(self, level: int = 1):
        try:
            filename = os.path.join('levels', f'{level}.txt')
            with open(filename, mode='r') as file:
                level_map = [line.strip() for line in file]

        except Exception:
            print('Error load level')
            self.terminate()
        self.scene = Level(self.screen, data=level_map)

    def terminate(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.start()
