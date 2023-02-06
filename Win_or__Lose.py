from settings import *


class WinOrLose:
    def __init__(self, surf: Surface, mode: str) -> None:
        self.mode = mode
        self.surf = surf
        self.image = None

        self.menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 328, 150, 60)),
                                                 text='Главное меню',
                                                 manager=manager)

        self.restart = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((560, 328, 150, 60)),
                                                    text='Начать с начала',
                                                    manager=manager)
        self.menu.hide()
        self.restart.hide()
        self.x = 0
        self.y = -600
        self.y1 = self.y2 = 700

    def render(self, mode: str) -> None:

        if mode == 'red win':
            self.image = pygame.image.load('data/red_win.png')
        elif mode == 'green win':
            self.image = pygame.image.load('data/green_win.png')

        self.surf.blit(self.image, (self.x, self.y))
        color = (255, random.randrange(1, 256), random.randrange(1, 256))
        pygame.draw.rect(self.surf, color, (268, self.y1, 155, 66), 10, 10)
        pygame.draw.rect(self.surf, color, (558, self.y2, 155, 66), 10, 10)

        if self.y < 0:
            self.y += FPS

        if self.y1 > 339:
            self.y1 -= FPS // 2
            self.menu.show()

        if self.y2 > 339:
            self.y2 -= FPS // 2
            self.restart.show()

        self.creating_particles()

    def creating_particles(self) -> None:
        for i in range(100):
            pygame.draw.rect(self.surf, (random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256)),
                             (random.randrange(10, 120), random.randrange(125, 640), 5, 10))
            pygame.draw.rect(self.surf, (random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256)),
                             (random.randrange(872, 972), random.randrange(125, 640), 5, 10))
