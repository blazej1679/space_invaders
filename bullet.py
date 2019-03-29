import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Klasa opisujaca pociski """

    def __init__(self, settings, ship):
        super().__init__()
        self.screen = settings.screen
        self.image = pygame.image.load('images/super_missile.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        self.y = float(self.rect.y)                     # zmienna przechowująca polozenie pocisku
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """ Zmiana polozenia pocisku """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def blit_bullet(self):
        """ Wyswietlenie pocisku """
        self.screen.blit(self.image, self.rect)
