from pygame import *
import random
import os

init()
display.set_caption('start')
size = (1100, 600)
screen = display.set_mode(size)

mass = []
backgrounds = (os.listdir(f'{os.path.abspath("data")}'))
for i in backgrounds:
    mass.append(image.load(f'data/{i}'))
image = mass[random.randrange(0, len(mass))]

clock = time.Clock()
running = True
count = 0
v = 30

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    screen.blit(image, (count, 0))
    if count > - 100:
        count -= v * clock.tick() / 1000
    else:
        image = mass[random.randrange(0, len(mass))]
        count = 0
    display.flip()
quit()
