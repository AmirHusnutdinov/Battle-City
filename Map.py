from settings import *


class TiledMap:
    def __init__(self, filename: str) -> None:
        tm = pytmx.load_pygame(filename, pixelalpha=True)

        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

        self.pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((980, 20, 100, 50)),
                                                      text='Pause',
                                                      manager=manager)
        self.back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((405, 300, 140, 40)),
                                                         text='Главное меню',
                                                         manager=manager)
        self.cansel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((555, 300, 140, 40)),
                                                   text='Отмена',
                                                   manager=manager)
        # Удали эти кнопку как появится смерть
        self.death = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0, 40, 40)),
                                                  text='Смэрть',
                                                  manager=manager)
        self.win = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 0, 40, 40)),
                                                text='win',
                                                manager=manager)

        self.pause = pygame.image.load('data/pause.png')

        self.pause_btn.hide()
        self.back_to_menu.hide()
        self.cansel.hide()

    def render(self, surf: Surface) -> None:
        # image = pygame.image.load('ind_zone/Background_new.png')
        #
        # surf.blit(image, (0, 0))
        # surf.blit(image, (1067, 0))

        self.back_to_menu.hide()
        self.cansel.hide()
        pygame.draw.rect(surf, 'black', (978, 18, 104, 54), 4, 10)

        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surf.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def open_pause(self, surf: Surface) -> None:
        self.back_to_menu.show()
        self.cansel.show()
        surf.blit(self.pause, (400, 200))

        pygame.draw.rect(surf, 'black', (397, 197, 307, 206), 4, 10)
        pygame.draw.rect(surf, 'black', (403, 299, 144, 43), 10, 4)
        pygame.draw.rect(surf, 'black', (553, 299, 144, 43), 10, 4)