from settings import *


class Walls(Sprite):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.image = load_image(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if self.rect.width < SPRITE:
            self.rect.x += (SPRITE - self.rect.width) // 2
        if self.rect.height < SPRITE:
            self.rect.y += (SPRITE - self.rect.height) // 2
        self.mask = pygame.mask.from_surface(self.image)


# class Wall1(Sprite):
#     sprite = 'IndustrialTile_73.png'
#
#
# class Wall2(Sprite):
#     sprite = 'IndustrialTile_04.png'
#
#
# class Wall3(Sprite):
#     sprite = 'IndustrialTile_13.png'
#
#
# class Wall4(Sprite):
#     sprite = 'IndustrialTile_05.png'
#
#
# class Wall5(Sprite):
#     sprite = 'IndustrialTile_06.png'
#
#
# class Wall6(Sprite):
#     sprite = 'IndustrialTile_15.png'
#
#
# class Wall7(Sprite):
#     sprite = 'IndustrialTile_16.png'
#
#
# class Wall8(Sprite):
#     sprite = 'IndustrialTile_14.png'
#
# class Wall9(Sprite):
#     sprite = 'IndustrialTile_67.png'
#
# class Wall10(Sprite):
#     sprite = 'IndustrialTile_22.png'
#
# class Wall11(Sprite):
#     sprite = 'IndustrialTile_24.png'
#
# class Wall12(Sprite):
#     sprite = 'IndustrialTile_17.png'
#
# class Wall13(Sprite):
#     sprite = 'IndustrialTile_23.png'
#
# class Wall14(Sprite):
#     sprite = 'IndustrialTile_13.png'
#
# class