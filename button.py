import pygame.sysfont


class Button():

    def __init__(self, settings, msg, pos_x, pos_y):
        """ inicjalizacja atrybutow przycisku """
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()

        # definiowanie wymiarow i wlasciwosci przycisku
        self.width, self.height = 200, 50
        self.button_color = (50, 150, 150)
        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # tworzenie przycisku i srodkowanie go
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = pos_x
        self.rect.centery = pos_y

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Umieszczenie komunikatu w wygenerowanym obrazie i wysrodkowanie """
        self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
