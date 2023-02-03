from settings import *


class Rules:
    def __init__(self) -> None:
        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((930, 20), (150, 50)),
                                                     text='Come back',
                                                     tool_tip_text='Press this Button!',
                                                     manager=manager)
        self.back_btn.hide()

    def render(self, surf: Surface) -> None:
        self.back_btn.show()
        pict2 = pygame.image.load('data/rules.png')
        graf2 = pict2.get_rect(bottomright=(1100, 600))
        surf.blit(pict2, graf2)