import pygame


class Settings(pygame.sprite.Sprite):
    """ Klasa do przechowywania ustawień gry. """
    def __init__(self, image_file='images/bg.jpg'):
        pygame.sprite.Sprite.__init__(self)                     # inicjalizacja sprite'a
        pygame.display.set_caption("Space Nut")

        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)   #dla innych rozdzielczosci
        self.screen = pygame.display.set_mode([1366, 768])

        # inicjalizacja zegara by ustalić FPS
        self.clock = pygame.time.Clock()

        self.bg_image = pygame.image.load(image_file)
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.left, self.bg_rect.top = [0, 0]

        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        # ustawienia pocisku
        self.amount_allowed_bullets = 3

        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """inicjalizacja ustawien zmieniejacych sie podczas gry"""
        self.ship_speed_factor = 0.4
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 2

        # punktacja
        self.alien_points = 50

    def increase_speed(self):
        """Zmiana szybkosci, wraz z postepem w grze"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def blit_bg(self):
        self.screen.blit(self.bg_image, self.bg_rect)
