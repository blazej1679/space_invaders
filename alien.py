import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.screen = settings.screen

        # wczytanie obrazu i pobranie rect
        self.image = pygame.image.load("images/alien_mid_purp.png")
        self.rect = self.image.get_rect()

        # umieszczenie obcego
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # dokladne polozenie x obcego
        self.x = float(self.rect.x)

    def blit_alien(self):
        """ Wyswietlenie obcego na jego aktualnym polozeniu """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ Wrtosc true przy dotknieciu krawedzi"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Ruch w prawo/lewo"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x
