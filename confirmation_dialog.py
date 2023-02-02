from settings import *


class ConfirmationDialog:
    def __init__(self) -> None:
        self.confirmation_dialog1 = None

    def open_confirmation_dialog(self) -> None:
        self.confirmation_dialog1 = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect((400, 100), (300, 200)),
            manager=manager,
            window_title='Confirm',
            action_long_desc='Вы уверены, что хотите выйти ?',
            action_short_name='YES',
            blocking=True)
        btn_sound.play()